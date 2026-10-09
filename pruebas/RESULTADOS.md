# Resultados de pruebas iniciales

Fecha: 4 de octubre de 2026.

## Resultado final

| Prueba | Resultado | Evidencia regenerable |
|---|---|---|
| PlantUML | Éxito: 9 fuentes renderizadas; SVG y PNG comprobados | `scripts/generacion/generar-plantuml.ps1` |
| Mermaid | Éxito: Gantt y arquitectura renderizados a SVG | `scripts/generacion/generar-mermaid.ps1` |
| draw.io | Éxito: XML con `mxfile`, `mxGraphModel`, formas, carriles y conectores | `scripts/generacion/generar_drawio.py` |
| DBML | Éxito: modelo analizado y convertido a PostgreSQL | `scripts/generacion/convertir-dbml.js` |
| DOT | Éxito: SVG generado con Viz.js | `scripts/generacion/generar-dot.js` |
| Documentos | Éxito: Markdown, CSV, DOCX, XLSX, PDF, PNG y SVG creados y reabiertos | `scripts/validacion/probar-formatos.py` |
| Integridad del proyecto | Éxito: 0 errores y 0 avisos | `scripts/validacion/validar_proyecto.py` |
| Seguridad npm | Sin vulnerabilidades moderadas o superiores; 5 bajas transitivas en KaTeX/Mermaid | `npm audit --audit-level=moderate` |
| Material didáctico | Éxito: 22/22, SHA-256 conforme, formatos correctos, 0 duplicados y 0 ilegibles | `scripts/validacion/inventariar_material.py` |
| GitHub | Éxito: autenticado; repositorio `PRIVATE`, rama predeterminada `main` | `scripts/instalacion/gh-local.ps1 auth status` y `repo view` |

## Incidencias corregidas

La primera prueba por lote reveló que los generadores PowerShell duplicaban la raíz cuando recibían rutas absolutas. Ambos scripts se corrigieron y la repetición completa terminó correctamente. La validación posterior también se ajustó para excluir `node_modules`, entornos virtuales y herramientas descargadas, evitando falsos positivos sobre archivos de terceros.

## Limitaciones verificadas

- `dot` y Pandoc no están instalados globalmente.
- PlantUML usa Smetana y DOT independiente usa Viz.js; no se cambió `PATH`.
- La corrección conceptual sigue requiriendo revisión humana contra el enunciado y los materiales académicos; los PDF/PPTX incorporados son rasterizados.
- Las salidas de prueba son regenerables y se excluyen de Git; las fuentes, scripts e informe sí se versionan.
