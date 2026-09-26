<?php
/**
 * Estratos · API de solo lectura.
 * Devuelve el modelo completo de AgileEA como JSON {tabla: [filas]} para la capa visual (index.html).
 * Usa las mismas credenciales que el ABM principal; ajustá CFG si cambian.
 */
// Entorno: true = Desarrollo (agileea_dev) / false = Producción (AgileEA)
const DEV = false;
const CFG = [
    'host' => 'localhost', 'port' => 3306,
    'user' => 'root', 'password' => '',
    'db'   => DEV ? 'agileea_dev' : 'AgileEA',
    'charset' => 'utf8mb4',
];

/* Tablas expuestas. Todo lo demás queda fuera (usuarios, configuración, etc.). */
const TABLAS = [
    'organizacion', 'capacidad_n1', 'capacidad_n2', 'capacidad_n3',
    'aplicacion', 'aplicacion_capacidad_n3', 'aplicacion_disciplina', 'aplicacion_organizacion', 'aplicacion_persona',
    'disciplina', 'persona', 'persona_organizacion', 'proveedor', 'proveedor_persona',
    'centro_costo', 'licencia', 'licencia_anual',
    'contrato', 'contrato_anio', 'contrato_anio_pagador', 'contrato_licencia',
    'contrato_costo_cabecera', 'contrato_costo_detalle',
    'glosario',
];

header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');

try {
    $pdo = new PDO(
        sprintf('mysql:host=%s;port=%d;dbname=%s;charset=%s', CFG['host'], CFG['port'], CFG['db'], CFG['charset']),
        CFG['user'], CFG['password'],
        [PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION, PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC]
    );
    $existentes = $pdo->query('SHOW TABLES')->fetchAll(PDO::FETCH_COLUMN);
    $out = ['_meta' => ['db' => CFG['db'], 'entorno' => DEV ? 'Desarrollo' : 'Producción', 'leido' => date('c')]];
    foreach (TABLAS as $t) {
        if (in_array($t, $existentes, true)) {
            $out[$t] = $pdo->query('SELECT * FROM `' . $t . '`')->fetchAll();
        }
    }
    echo json_encode($out, JSON_UNESCAPED_UNICODE);
} catch (Throwable $e) {
    error_log('Estratos api.php: ' . $e->getMessage());
    http_response_code(503);
    echo json_encode(['error' => 'No se pudo leer la base de datos ' . CFG['db'] . '. Revisá CFG en estratos/api.php.'], JSON_UNESCAPED_UNICODE);
}
