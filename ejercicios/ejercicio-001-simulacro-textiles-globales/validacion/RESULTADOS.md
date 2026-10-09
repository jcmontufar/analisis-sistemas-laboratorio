# Resultados de validación — 8 de octubre de 2026

Estado: entrega local terminada, pendiente de revisión humana. Sin commit ni publicación.

SHA-256 del PDF original: `97B0B4F60A010FCA32062FBD7240A1505275625C6FA46A7FCAD14005F0F1C239`.
Archivo real: `enunciado/Simulacro de examen .pdf`; nombre y contenido preservados. Sus dos páginas se leyeron, extrajeron y revisaron antes de dibujar. Comparación contra Texto pegado.txt en `enunciado/COMPARACION.md`; el PDF gobierna los hechos, el texto complementa entrega y validación.

## VALIDACIÓN SINTÁCTICA

- Validador del laboratorio: scripts/validacion/validar_proyecto.py con .venv/Scripts/python.exe: 0 errores, 0 avisos.
- Validador específico: evidencias/validar_ejercicio.py con Python documental; detalle en comprobaciones.json: cero fallos.
- Seis XML DRAW.IO editables mxfile/mxGraphModel, conectores con referencias existentes.
- Seis PDF individuales de una página, seis SVG válidos y seis PNG decodificables, no vacíos. Exportación nativa DRAW.IO Desktop 32.3.0.
- DOCX válido con trece apartados principales y seis diagramas. PDF final de 22 páginas.
- Escaneo textual de patrones de tokens GitHub, claves AWS y claves privadas: sin coincidencias. No es garantía universal de ausencia de secretos.

## VALIDACIÓN ESTRUCTURAL

Contexto: un proceso 0 y cuatro entidades humanas. Nivel 0: cuatro procesos y cuatro almacenes, todos con entrada y salida; sin conexión directa entidad/almacén ni almacén/almacén.
Balance exacto F01–F08 por actor, dirección y nombre, normalizando solo espacios visuales.
UML: cinco include hacia el comportamiento incluido y un extend de rechazo hacia inspección, con guarda.
Secuencia/colaboración: veinte mensajes idénticos en número, emisor, receptor y contenido. Alternativas 14/15 excluyentes; ciclo 13–17 por prenda; 18–20 si hay aprobadas.
Vértices dentro del lienzo; nombres de archivo coincidentes. Matriz manual en CONSISTENCIA.md.

## VALIDACIÓN ACADÉMICA

Se contrastaron el original y las matrices pertinentes del laboratorio, sin imponer mínimos DERCAS ajenos al examen. Se conservan campos de OT, metraje frente a estándar, conteo/merma, avance por paquete, tiempo por lote e inspección individual con clasificación y causas.
Se justifican cuatro almacenes; D4 consolida inspecciones y lotes liberados. El ID interno antecede al código de empaque. Confirmaciones y consulta de coordinación son inferencias. Solo aprobadas se liberan; rechazadas quedan registradas, sin inventar reproceso. Include expresa obligación y extend condición, no navegación.

Factibilidad operativa condicionada a formación práctica y piloto, sin afirmar aceptación probada. Técnica: monolito Django/PostgreSQL en nube administrada, condicionado a conectividad; terminal y tableta son alternativas. Económica: inversión y operación parametrizadas, sin precios/empleados/ahorros ficticios ni doble contabilización de suscripciones. ROI y recuperación requieren cotizaciones y mediciones.

No es certificación del catedrático: revisar fórmula/unidad de merma, tolerancias, lote-paquete, liberaciones parciales, rechazadas, estaciones/turnos, RPO/RTO, conectividad, moneda, precios y beneficios.

## REVISIÓN VISUAL

Revisadas las seis exportaciones y todas las 22 páginas del documento final. Evidencias: evidencias/revision-diagramas/ y evidencias/revision-documento/final-01.png a final-22.png. Las imágenes pagina-* son la iteración anterior.

Se corrigieron etiquetas solapadas del DFD, enlaces compartidos de colaboración, marcos loop/alt y separación de alternativas. No se observan cortes finales. Prosa Letter; láminas proporcionalmente ampliadas para conservar legibilidad. Reducir todo a Letter perjudica las etiquetas.

render_docx.py --emit_pdf falló por ausencia de LibreOffice soffice.exe. El DOCX se exportó con Microsoft Word instalado, ExportAsFixedFormat; PDF renderizado con Poppler y revisado. Se distingue el fallo de la herramienta canónica del éxito de la alternativa.

## Alcance y revisión humana

El validador general reconoce carpetas ejercicio-NNN: el nombre ampliado solicitado no acredita completitud automáticamente. Por ello se añadieron controles específicos.
Completar nombre/carné y aprobar inferencias/datos. Agregar hescobarm@miumg.edu.gt como colaborador es instrucción del PDF pendiente para después de revisión/autorización de compartir. No se compartió contenido externamente.

## Git

Rama codex/ejercicio-001-textiles-globales. HEAD conservado: a188e4083c016dd798c7ea93ac62792842db4802. Cambios solo dentro del ejercicio; sin staged, commit ni push.

## Revisión 1.1

Revisión puntual solicitada el 8 de octubre de 2026. Las secciones anteriores describen la entrega inicial; esta sección identifica la revisión vigente.

1. Stack reorganizado en Planta, Perímetro y Nube, con espaciado y jerarquía. Router/firewall separado de Internet; HTTPS es etiqueta de enlace. Tecnologías seleccionadas preservadas, nube condicionada a conectividad/energía, RPO 24 h y RTO 8 h propuestos, no garantías.
2. F04 = «Datos de corte y estado del registro»; F06 = «Datos de paquete habilitado y estado de confección». Nombres idénticos en ambos DFD, análisis, matriz, DOCX/PDF y comprobaciones. Los otros seis flujos no cambian.
3. Eliminado P4→P1. P4 actualiza D4 y P1 consulta D4 mediante «Resumen de calidad y lote liberado» para producir F02. D4 se representa también cerca de P1 como el mismo almacén lógico: no es D5 ni una copia física. El enlace se limita al corredor de P1, sin atravesar todo el borde inferior.
4. Caso de uso «Liberar aprobadas para empaque», con include hacia Generar código de lote y precondición de aprobadas. No se atribuye empaque físico al Inspector; se registra A08 sobre el ejecutor/registro físico no especificado. P4 y los demás procesos, actores y relaciones no cambian.
5. Mensaje 20 = «Código de lote y confirmación de liberación». Los mensajes 1–19, loop, alt y condición de aprobadas se conservan. La confirmación prueba liberación registrada, no empaque físico ejecutado.
6. Colaboración con llamadas abreviadas numeradas sobre enlaces separados, guardas de aprobada/rechazada/hay aprobadas y tabla inferior con los veinte contenidos completos. Emisores y receptores idénticos a secuencia.

Resultado vigente: 84 comprobaciones específicas PASS, cero fallos; validador general del laboratorio: 0 errores y 0 avisos. Los controles anteriores se mantienen y se añaden pruebas de regresión de actores, mensajes, flujos no modificados, equivalencia de enlaces, zonas del stack y preservación SHA-256 de las tres factibilidades. También se comparan los bytes SHA-256 de las seis imágenes incrustadas en DOCX contra las PNG oficiales.

Se regeneraron los seis PDF/SVG/PNG con DRAW.IO Desktop 32.3.0; cada PDF individual conserva una página. Fuentes DRAW.IO nativas editables. Documento actualizado: 22 páginas y trece apartados, con seis láminas reemplazadas. Prosa y factibilidades conservan estructura, estilo y contenido, salvo las actualizaciones puntuales de análisis, matriz y descripciones solicitadas.

Revisión visual: las seis exportaciones PDF rasterizadas y las 22 páginas del documento fueron inspeccionadas; se corrigieron etiquetas y corredores de DFD 0/colaboración. Sin texto cortado ni conectores ajenos atravesando etiquetas en los diagramas finales. Vértices dentro del lienzo. Evidencias vigentes: evidencias/revision-1.1/diagramas/ y evidencias/revision-1.1/documento/. Las evidencias anteriores se conservan como historial, no como entrega vigente.

La herramienta canónica render_docx.py no encontró LibreOffice soffice.exe. Alternativa utilizada: Microsoft Word instalado, ExportAsFixedFormat. Diagramas rasterizados con Poppler; las evidencias vigentes de las 22 páginas del informe proceden de PDFium. No se afirma que la herramienta canónica haya funcionado. Se conserva la tipografía original del informe, incluyendo encabezados y pies, cuya presencia se contrastó mediante extracción y evidencia rasterizada.

Inventario exacto de archivos modificados y nuevos: ARCHIVOS-REVISION-1.1.md, comparado por SHA-256 contra evidencias/revision-1.1/linea-base.json. Todo el trabajo permanece dentro del ejercicio. El PDF original y las tres factibilidades no se modificaron.

Persisten las ambigüedades A01–A08: dotación/turnos/cobertura, perfil del Jefe, tolerancias, lote-paquete/código/liberaciones parciales, rechazadas, cotizaciones/métricas, conectividad/energía y empaque físico. Revisar además fórmula/unidad de merma, inferencias de liberación y objetivos RPO/RTO; completar nombre/carné. El colaborador externo sigue pendiente de autorización de compartir.

Rama y HEAD conservados; índice vacío. No se ejecutó commit ni push. Detenido para revisión humana.

## Cierre final

La revisión humana de la versión 1.1 fue aprobada por el usuario. En este cierre únicamente se actualizaron estados editoriales: portada a «Estado: versión final revisada del simulacro académico. No constituye una implementación ni una inversión autorizada.» y pies de página a «Versión final revisada». Se conservaron los números de página, encabezados, estilos, tamaños, imágenes y demás elementos. Estudiante y carné permanecen en blanco por tratarse de un simulacro; esta instrucción sustituye los pendientes históricos de completar esos campos.

El DOCX se actualizó mediante sustituciones puntuales en sus componentes OOXML, y su generador conserva las mismas dos sustituciones para futuras regeneraciones. Todos los componentes del DOCX son idénticos a la versión 1.1 salvo el texto de portada en document.xml y el estado en footer1.xml. No se modificaron las factibilidades, análisis, arquitectura, flujos, actores ni mensajes. Las seis fuentes DRAW.IO y sus dieciocho exportaciones PDF/SVG/PNG permanecen idénticas por SHA-256 a la versión 1.1; tampoco se regeneraron ni rediseñaron diagramas.

El PDF se regeneró con Microsoft Word mediante ExportAsFixedFormat. render_docx.py volvió a fallar por ausencia de LibreOffice soffice.exe; se utilizó la alternativa de Word y rasterizado PDFium. Las 22 páginas se revisaron visualmente: sin cortes y con los seis diagramas legibles. Comparación de texto página a página idéntica tras aplicar únicamente las dos sustituciones autorizadas; las páginas 2–22 son idénticas píxel a píxel fuera del área del pie. No aparecen «Revisión humana pendiente» ni «Sin commit ni publicación» en DOCX/PDF. Los textos históricos de entrega y pendientes técnicos no se reescribieron para preservar el alcance aprobado.

Validaciones repetidas: 84 comprobaciones específicas PASS, cero fallos; validador general del laboratorio: cero errores y cero avisos. Fuentes y exportaciones presentes, imágenes incrustadas idénticas a las PNG oficiales y PDF original preservado con SHA-256 `97B0B4F60A010FCA32062FBD7240A1505275625C6FA46A7FCAD14005F0F1C239`. Escaneo de patrones de credenciales sin coincidencias; se mantiene la limitación de que no es garantía universal de ausencia de secretos.

Respecto al inicio de este cierre solo cambiaron cuatro archivos: documentos/Solucion-Textiles-Globales.docx, documentos/Solucion-Textiles-Globales.pdf, evidencias/generar_documento.py y este RESULTADOS.md. Las evidencias visuales históricas de la revisión 1.1 se conservaron; la inspección del cierre utilizó imágenes temporales fuera del repositorio.

Cierre de Git autorizado: commit descriptivo del ejercicio completo y publicación únicamente de codex/ejercicio-001-textiles-globales en el repositorio privado. Sin fusión con main y sin agregar colaboradores externos. Las secciones anteriores conservan el historial de las entregas previas, no el estado editorial vigente.
