# Matrices de evaluación

Leyenda: **A** = exigencia académica explícita; **C** = convención técnica complementaria. Las comprobaciones automáticas detectan estructura, texto o relaciones declaradas; la corrección semántica y la legibilidad final siempre requieren juicio humano.

| Artefacto | Criterios A (fuente) | Criterios C | Automático | Humano |
|---|---|---|---|---|
| Requerimientos | RF con ID, verbo+sustantivo, actor, entradas, salidas, prioridad; RNF con métrica/condición; completos, verificables y trazables (PDF 05, págs. 8–11). DERCAS: permiso, método/fechas, entrevista por proceso y 2 encuestas (instrucciones, “Ingeniería…”, PPTX d. 6) | Criterios de aceptación, versión, responsable | IDs únicos; campos; métricas numéricas cuando proceda | Necesidad correcta, no ambigua, factible y trazable |
| Factibilidad | Operativa/técnica/económica con contenidos y tablas detalladas (instrucciones DERCAS, “Factibilidad”; PPTX d. 9) | Supuestos, moneda, horizonte, riesgo | Sumas, subtotales, mensual×12, campos | Evidencia, realismo y conclusión |
| Proceso técnico | Español estructurado y procesos primitivos (PDF 05, págs. 12–13); DERCAS exige descripción por proceso | Pre/postcondiciones y excepciones | Secciones y palabras de control | Ambigüedad y completitud |
| Listado de pasos | Número, nombre, descripción y responsable (instrucciones DERCAS, “Procesos a automatizar”; PNG 10 ejemplo) | Numeración estable y acción observable | Secuencia/duplicados/campos | Nivel de detalle y continuidad |
| Diagrama de flujo con carriles verticales | Al menos una decisión por flujo DERCAS (instrucciones; PPTX d. 7) | Inicio/fin, guardas y un carril vertical por responsable cuando el ejercicio lo pida | Nodos inicio/fin/decisión, salidas y orientación de carriles | Flujo lógico, cruces y responsabilidad |
| Arquitectura/stack | Usuario→frontend→internet→nube→backend/BD; explicación del conjunto y tecnologías (instrucciones “Stack”; PPTX d. 8) | Interfaces, protocolos, justificación por RNF | Componentes/nombres/enlaces | Viabilidad, seguridad y coherencia |
| DFD contexto | Proceso 0 con nombre del sistema, entidades y flujos (instrucciones “DFD Contexto”; PPTX d. 8) | Flujos nombrados/orientados, sin almacenes | Un proceso, número 0, etiquetas | Frontera, entidades y naturaleza de datos |
| DFD nivel 0 | 2–3 pasos principales por proceso, flujos nombrados, almacén por proceso, entrada/salida (instrucciones “DFD Nivel 0”) | Balance con contexto; sin entidad–almacén | Numeración, almacenes, grados de conexión | Balance semántico y descomposición |
| Entidad–relación | DERCAS: ≥40 tablas distribuidas por proceso (instrucciones “Entidad Relación”; PPTX d. 8) | Claves, cardinalidades, normalización | Conteo, PK/FK y relaciones | Pertinencia, redundancia y cardinalidad |
| Diccionario de datos | Resumen con conteos de tablas/campos/PK/FK y enlace completo (instrucciones DERCAS) | Tipo, longitud, dominio, nulabilidad, definición | Conteos y referencias | Significado y consistencia transversal |
| Prototipos | Pantallas principales y descripción; lógica no revisada en esa sección (instrucciones “Prototipo”) | Actor, requisito, datos, estados, fidelidad | Presencia/enlaces/IDs | Usabilidad y cobertura |
| UML casos de uso | General tras login y uno por flujo (instrucciones DERCAS, “Anexos”) | Actores/límite; semántica include/extend | Actores, casos, límite, estereotipos | Valor observable y relaciones |
| UML clases | Correspondencia exacta con ER (instrucciones DERCAS, “Anexos”) | Atributos, operaciones, multiplicidades | Nombres/relaciones vs ER | Abstracción y responsabilidades |
| UML secuencia | Uno por cada flujo (instrucciones DERCAS, “Anexos”) | Líneas de vida, orden temporal, mensajes, respuestas y condiciones | Cobertura, participantes y mensajes | Orden, condiciones y resultado |
| UML colaboración | Uno por cada flujo (instrucciones DERCAS, “Anexos”) | Vínculos y mensajes numerados; equivalencia con secuencia | Cobertura, numeración y conjunto de participantes | Orden lógico y equivalencia semántica |
| Otros UML: actividad, estados, componentes, despliegue | Componentes de módulos; despliegue basado en stack; estados por flujo (instrucciones DERCAS, “Anexos”) | Notación UML coherente y vocabulario común | Tipos de nodo y referencias | Comportamiento, dependencias y despliegue realista |
| Cronograma | ≥45 actividades específicas con responsable/departamento/instrumento (instrucciones “Cronograma”; PPTX d. 10) | Dependencias, hitos, entregables | Conteo, fechas, precedencias | Duración, granularidad y viabilidad |

## Contradicciones y decisiones

1. La regla general del laboratorio no impone mínimos de tablas; DERCAS exige 40. Se aplica el mínimo solo a entregas DERCAS.
2. “UML de Contexto” figura como anexo, pero no es un tipo UML estándar. Debe conservarse como requisito pendiente de aclaración, no reinterpretarse automáticamente.
3. Los PNG son ejemplos, no rúbrica. Errores potenciales (duplicación de “Cliente” en PNG 14 y uso dudoso de `extend` en PNG 11) no se propagan.
4. En una tensión entre PPTX resumido y Markdown detallado, se cumplen ambos si son compatibles; una contradicción material se eleva al catedrático.

## Carencias que impiden automatización total

No se define notación DFD exacta por defecto, herramienta de diagramación, escala de prioridad, criterios de aceptación, normalización de datos, umbral de factibilidad, fidelidad de prototipo ni significado de “UML de Contexto”. Tampoco hay fuentes editables de los ejemplos rasterizados.
