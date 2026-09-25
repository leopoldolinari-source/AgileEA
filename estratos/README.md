# Estratos

Capa de consumo visual para AgileEA. No reemplaza el ABM (`index.php`): lee la misma base y la presenta en seis vistas conectadas.

| Vista | Qué responde |
|---|---|
| Mapa | Matriz de capacidades: clasificación (vertical) × etapas de la cadena de valor (horizontal), con los dominios N1 como filtro. Filas y etapas se ocultan con un clic. Alternativa "Estratos": un estrato por dominio. Lentes de color: dominio, cobertura, criticidad, pace layering, madurez, impacto regulatorio |
| Consultar | Preguntas en lenguaje natural sobre el modelo. La respuesta enlaza cada entidad a su ficha y puede resaltar sus capacidades en el mapa |
| Red | Grafo de todo el modelo (orgs, apps, proveedores, contratos, licencias, personas, CeCos). Un clic aísla el vecindario |
| Portafolio | Matriz TIME (ajuste funcional × técnico), burbuja = gasto del año, color = lifecycle |
| Flujo de costos | Sankey proveedor → aplicación → organización pagadora → centro de costo, filtrable por año |
| Horizonte | Línea de tiempo de contratos con alertas de vencimiento |
| Salud del modelo | Índice de completitud y lista priorizada de acciones |

Además: ficha lateral navegable para cualquier entidad y búsqueda global con `Ctrl K`.

## Instalación

Copiar la carpeta `estratos/` junto al `index.php` del ABM. Ajustar `CFG` en `estratos/api.php` si difiere.
Opcional: agregar al menú lateral del ABM `<a class="it" href="estratos/">Estratos</a>`.

## Fuentes de datos

`index.html` intenta, en orden:
1. `api.php` — base viva (solo lectura, tablas en lista blanca). Por defecto lee **producción** (`AgileEA`); `DEV = true` pasa a `agileea_dev`. Si falla, la página muestra el error: no cambia sola al backup.
2. `data.json` — solo si no hay `api.php` (por ejemplo, el link de claude.ai). Se muestra un aviso de "datos de demostración". Se genera así:
   `python3 tools/sql_to_json.py agileEA_backup.sql estratos/data.json`
   (`data.json` está en `.gitignore` porque contiene datos del negocio.)

D3 se carga del CDN; si la red lo bloquea, usa las copias de `lib/`.

## Consulta en lenguaje natural (`ask.php`)

La vista "Consultar" envía el modelo serializado (~40 KB) y la pregunta a Claude.

- Dentro de claude.ai usa la cuenta de quien mira la página.
- En el servidor propio usa `ask.php`:
  1. `cd estratos && composer require "anthropic-ai/sdk"`
  2. Definir `ANTHROPIC_API_KEY` en el entorno del servidor web.
  3. Por defecto solo responde a usuarios con sesión iniciada en AgileEA (`ASK_SOLO_ADMIN`) y hasta 60 consultas por hora por sesión. Ajustable al inicio del archivo.

Modelo: `claude-opus-5`. El modelo serializado va como system prompt cacheado, así las preguntas siguientes cuestan menos.
