<?php
/**
 * Estratos · Consulta en lenguaje natural.
 *
 * Recibe {system, messages} desde index.html (vista "Consultar") y responde {text}.
 * `system` trae las instrucciones y el modelo serializado; `messages` la conversación.
 *
 * Requisitos:
 *   composer require "anthropic-ai/sdk"        (dentro de estratos/)
 *   Variable de entorno ANTHROPIC_API_KEY en el servidor web.
 */

/* Cada consulta tiene costo en la cuenta de la API: por defecto solo la usa quien inició sesión en AgileEA. */
const ASK_SOLO_ADMIN = true;
const ASK_MODELO = 'claude-opus-5';
const ASK_MAX_CONSULTAS_POR_HORA = 60;
const ASK_MAX_BYTES = 200000;

require __DIR__ . '/vendor/autoload.php';

use Anthropic\Client;
use Anthropic\Core\Exceptions\APIConnectionException;
use Anthropic\Core\Exceptions\APIStatusException;
use Anthropic\Core\Exceptions\AuthenticationException;
use Anthropic\Core\Exceptions\RateLimitException;

session_start();
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

function responder(int $status, array $body): void {
    http_response_code($status);
    echo json_encode($body, JSON_UNESCAPED_UNICODE);
    exit;
}

if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    responder(405, ['error' => 'metodo', 'message' => 'Usá POST.']);
}
if (ASK_SOLO_ADMIN && empty($_SESSION['migae_admin'])) {
    responder(401, ['error' => 'login']);
}

// Límite simple por sesión
$ahora = time();
$_SESSION['estratos_ask'] = array_values(array_filter($_SESSION['estratos_ask'] ?? [], fn($t) => $t > $ahora - 3600));
if (count($_SESSION['estratos_ask']) >= ASK_MAX_CONSULTAS_POR_HORA) {
    responder(429, ['error' => 'rate_limited']);
}
$_SESSION['estratos_ask'][] = $ahora;
session_write_close();

$raw = file_get_contents('php://input');
if ($raw === false || strlen($raw) > ASK_MAX_BYTES) {
    responder(413, ['error' => 'prompt_too_large']);
}
$in = json_decode($raw, true);
$system = is_array($in) ? ($in['system'] ?? null) : null;
$mensajes = is_array($in) ? ($in['messages'] ?? null) : null;
if (!is_string($system) || !is_array($mensajes) || !$mensajes) {
    responder(400, ['error' => 'invalid_request', 'message' => 'Faltan system o messages.']);
}
$limpios = [];
foreach ($mensajes as $m) {
    $rol = $m['role'] ?? '';
    $txt = $m['content'] ?? '';
    if (!in_array($rol, ['user', 'assistant'], true) || !is_string($txt) || trim($txt) === '') {
        responder(400, ['error' => 'invalid_request', 'message' => 'Mensaje inválido.']);
    }
    $limpios[] = ['role' => $rol, 'content' => $txt];
}
if (end($limpios)['role'] !== 'user') {
    responder(400, ['error' => 'invalid_request', 'message' => 'La conversación debe terminar en una pregunta.']);
}

$apiKey = getenv('ANTHROPIC_API_KEY');
if (!$apiKey) {
    responder(503, ['error' => 'sin_backend']);
}

try {
    $client = new Client(apiKey: $apiKey);
    $respuesta = $client->messages->create(
        model: ASK_MODELO,
        maxTokens: 16000,
        thinking: ['type' => 'adaptive'],
        // El modelo serializado es estable entre preguntas: se cachea.
        system: [
            ['type' => 'text', 'text' => $system, 'cacheControl' => ['type' => 'ephemeral']],
        ],
        messages: $limpios,
    );

    if ($respuesta->stopReason === 'refusal') {
        responder(200, ['error' => 'refused']);
    }
    $texto = '';
    foreach ($respuesta->content as $bloque) {
        if ($bloque->type === 'text') {
            $texto .= $bloque->text;
        }
    }
    if (trim($texto) === '') {
        responder(502, ['error' => 'empty_completion']);
    }
    responder(200, ['text' => $texto]);
} catch (AuthenticationException $e) {
    responder(503, ['error' => 'sin_backend']);
} catch (RateLimitException $e) {
    responder(429, ['error' => 'rate_limited']);
} catch (APIStatusException $e) {
    responder(502, ['error' => 'upstream_error', 'message' => 'La API de Claude devolvió un error.']);
} catch (APIConnectionException $e) {
    responder(502, ['error' => 'upstream_error', 'message' => 'No se pudo conectar con la API de Claude.']);
}
