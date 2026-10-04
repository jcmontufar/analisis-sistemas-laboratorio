# Herramientas del laboratorio

Este archivo se actualiza con `scripts/instalacion/comprobar-entorno.ps1` y con los resultados de `pruebas/RESULTADOS.md`.

## Política

Las dependencias se instalan dentro del proyecto. No se modifican `PATH`, Git global ni otras configuraciones globales de Windows. `herramientas-locales/`, `node_modules/` y `.venv/` son regenerables y no se versionan.

## Inventario verificado (4 de octubre de 2026)

| Componente | Versión/estado |
|---|---|
| Git | 2.55.0.windows.5 |
| GitHub CLI portátil | 2.102.0; instalado localmente, sin autenticación |
| Java | 23 (2024-09-17) |
| PlantUML | 1.2026.8; JAR local |
| Node.js / npm | 24.21.0 / 11.19.0 |
| Mermaid CLI | 11.17.0; instalado localmente y renderizado con éxito |
| DBML Core | 10.2.0; conversión PostgreSQL verificada |
| Viz.js | 3.31.0; motor DOT local verificado |
| Python | 3.12.5; entorno virtual local |
| `dot` del sistema | no disponible en `PATH`; se usa Smetana o Viz.js |
| Pandoc | no disponible; no es necesario para las pruebas actuales |

## Función de cada herramienta

| Herramienta | Uso | Salidas |
|---|---|---|
| PlantUML | UML, actividades, estados, componentes y despliegue | SVG, PNG |
| Mermaid CLI | Flujo, Gantt, procesos y arquitectura sencilla | SVG, PNG, PDF |
| Graphviz / Viz.js | Motor de disposición y validación DOT | SVG, PNG |
| draw.io XML | Diagramas editables con formas, conectores y carriles | `.drawio` |
| DBML Core | Validación del modelo y conversión a SQL sin conectores innecesarios | DBML, SQL |
| Python | Validación y producción documental | Markdown, PDF, DOCX, CSV, XLSX, SVG, PNG |

## draw.io

Un `.drawio` válido es XML con raíz `mxfile`, al menos un `diagram` y un `mxGraphModel`. El generador incluido crea celdas editables, geometrías y conectores; la validación analiza la estructura XML en vez de asumir editabilidad por la extensión.

## DBML

DBML conserva tablas, tipos, claves primarias, referencias y cardinalidades en texto versionable. `@dbml/core` valida y convierte el ejemplo a SQL mediante un script local. Se evitó `@dbml/cli` porque incorpora conectores no requeridos y dependencias con avisos de seguridad. La representación visual puede abrirse en una herramienta compatible; la fuente DBML es el artefacto canónico.

## Graphviz

El comando global `dot` no está disponible. Para no modificar Windows, las plantillas PlantUML que requieren disposición usan Smetana, el motor Java integrado, y los archivos DOT independientes se renderizan con `@viz-js/viz`. Ambas rutas se probaron localmente.
