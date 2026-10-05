# Informe de incorporación del material didáctico

Fecha: 4 de octubre de 2026.

## Resultado

Se procesaron 22 originales: 18 PNG, 2 PDF, 1 PPTX y 1 Markdown. No se modificó su contenido. Al inicio estaban en la raíz del proyecto, no en la carpeta anunciada; se trasladaron por nombre exacto a `material-didactico/originales/` y se comprobó que los SHA-256 no cambiaran.

- Integridad: 22/22 coinciden con la línea base `manifiesto-sha256.txt`; 0 corruptos, 0 duplicados y 0 ilegibles.
- PDF: 15 páginas cada uno, sin texto nativo; revisión visual completa.
- PPTX: 11 diapositivas compuestas por imágenes, sin texto nativo; revisión visual completa.
- PNG: 18 imágenes revisadas visualmente.

## Base de conocimiento

Se incorporaron fichas o síntesis sobre sistemas de información, ciclo de vida/cascada/incremental/RUP, levantamiento y especificación de requerimientos, DERCAS y prototipos, factibilidad, descripción/listado/flujo/cronograma de procesos, arquitectura/stack/despliegue, DFD contexto/nivel cero, UML y modelado/diccionario de datos. Las 15 matrices solicitadas están en `base-conocimiento/criterios-evaluacion/README.md`.

Cada síntesis distingue reglas académicas explícitas, convenciones complementarias, ejemplos, fuentes y vacíos. La prueba con las seis consultas pedidas está en `base-conocimiento/consultas-recuperacion.md`.

## Vacíos y revisión humana

- No se define por defecto notación DFD, herramienta de diagramación, escala de prioridad, normalización, umbral financiero ni fidelidad del prototipo.
- “UML de Contexto” es un rótulo académico ambiguo y requiere aclaración.
- No hay ejemplos originales de UML de clases ni componentes.
- PNG 11 usa `extend` de manera dudosa; PNG 14 duplica “Cliente”; se documentaron sin alterar.
- PNG 17 tiene alta densidad de rótulos; todo material rasterizado requiere revisión humana si se necesita transcripción literal.

## Pruebas

| Comprobación | Resultado |
|---|---|
| Inventario, formatos, SHA-256, duplicados y apertura | 0 errores |
| Estructura, fuentes editables, XML y enlaces Markdown | 0 errores, 0 avisos |
| Escritura/reapertura de MD, CSV, DOCX, XLSX, PDF, PNG y SVG | Éxito |
| Recuperación de conocimiento | 6/6 respuestas con archivo de origen |
| Escaneo de patrones de credenciales en archivos preparados | Sin coincidencias |
| GitHub CLI | Sesión activa por HTTPS |
| Privacidad remota | `PRIVATE` |

## Estado de publicación

Los cambios se publican en `main`. La confirmación final de commit, remoto y sincronización se obtiene después del push con `git status`, `git rev-parse` y GitHub CLI.
