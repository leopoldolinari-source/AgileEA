# Estratos

Capa de consumo visual para AgileEA. No reemplaza el ABM (`index.php`): lee la misma base y la presenta en seis vistas conectadas.

| Vista | Qué responde |
|---|---|
| Mapa | Capacidades N1 → N2 → N3 como estratos, con lentes: cadena de valor, clasificación, cobertura, criticidad, pace layering, madurez, impacto regulatorio |
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
1. `api.php` — base viva (solo lectura, tablas en lista blanca).
2. `data.json` — exportado de un backup, para demo sin base:
   `python3 tools/sql_to_json.py agileEA_backup.sql estratos/data.json`
   (`data.json` está en `.gitignore` porque contiene datos del negocio.)

D3 se carga del CDN; si la red lo bloquea, usa las copias de `vendor/`.
