# Matrices de evaluación auditadas

Cada criterio tiene una sola clasificación:

- `ACADEMICO_EXPLICITO`: el material lo ordena o define expresamente.
- `EJEMPLO_ACADEMICO`: se observa en una imagen, sin convertirse por ello en obligación.
- `TECNICO_COMPLEMENTARIO`: convención técnica para mejorar corrección y consistencia.
- `INFERENCIA`: conclusión razonable, no literal.
- `AMBIGUO`: la evidencia no permite una decisión segura.

Los requisitos identificados como DERCAS no se aplican automáticamente a ejercicios individuales. “Automático” comprueba presencia o estructura, nunca corrección académica.

## 1. Factibilidad técnica, operativa y económica

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Introducción con fechas y resumen de cada factibilidad | ACADEMICO_EXPLICITO | `11-InstruccionesDeRevisionDERCAS.md`, línea 39; PPTX DERCAS, diap. 9 | Secciones y fechas | Pertinencia del resumen |
| Operativa: usuarios, conocimiento técnico, fecha de encuesta y capacitaciones | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 39 | Campos y fecha | Evidencia y suficiencia |
| Técnica: equipo actual y necesario, sin precios | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 39 | Tablas/campos; ausencia de columnas monetarias | Realismo y capacidad |
| Económica: al menos tres tablas, servicios ×12, implementación por semanas, subtotales y conclusiones | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 39 | Conteo y aritmética | Supuestos y costos omitidos |
| Moneda, horizonte, riesgos y sensibilidad | TECNICO_COMPLEMENTARIO | Sin fuente académica expresa | Campos y fórmulas | Idoneidad financiera |

## 2. Cronograma de actividades

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Mínimo 45 actividades en DERCAS | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 40; PPTX, diap. 10 | Conteo | Aplicabilidad a DERCAS |
| Actividades no genéricas; indicar persona/departamento/instrumento | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 40 | Campos y términos vacíos | Especificidad |
| Fechas, duraciones, dependencias e hitos coherentes | TECNICO_COMPLEMENTARIO | Sin regla literal en el material | Fechas y precedencias | Viabilidad |
| Aplicar 45 actividades a cualquier ejercicio | AMBIGUO | La fuente solo lo ubica en “Cronograma del Proyecto” DERCAS | No | Debe decidirlo el enunciado |

## 3. Proceso técnico

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Incluir descripción técnica del proceso | ACADEMICO_EXPLICITO | Instrucciones DERCAS, líneas 26–27 | Presencia | Precisión |
| Usar español estructurado y descomponer hasta procesos primitivos | ACADEMICO_EXPLICITO | `05-Requirements_Engineering.pdf`, págs. 12–13 | Palabras de control | Ambigüedad y atomicidad |
| Narrativa separada por procesos | EJEMPLO_ACADEMICO | `09-DescripcionDelProceso.png`, imagen completa | Encabezados | Correspondencia con el dominio |
| Objetivo, alcance, entradas, salidas, pre/postcondiciones y excepciones | TECNICO_COMPLEMENTARIO | Sin listado académico completo | Secciones | Completitud semántica |

## 4. Listado de pasos

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Número, nombre, descripción y responsable | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 28 | Columnas y valores | Responsabilidad correcta |
| Descomposición hasta pasos primitivos | ACADEMICO_EXPLICITO | PDF 05, pág. 13 | Profundidad/numeración | Atomicidad |
| Numeración jerárquica de actividades y subactividades | EJEMPLO_ACADEMICO | `10-DescripcionProceso.png`, imagen completa | Patrón numérico | Orden lógico |
| Identificadores estables y una acción observable por paso | TECNICO_COMPLEMENTARIO | Sin regla literal | Duplicados y verbos | Granularidad |

## 5. Diagrama de flujo con carriles verticales

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Al menos una decisión por diagrama DERCAS | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 29; PPTX, diap. 7 | Nodo de decisión y salidas | Decisión real |
| Carriles por Administrador, Usuario y Sistema | EJEMPLO_ACADEMICO | `16-DiagramaDeActividades.png`, imagen completa | Nombres de carril | Roles pertinentes |
| Inicio/fin, acciones, guardas y flujo dirigido | TECNICO_COMPLEMENTARIO | Convención UML/flujo | Tipos de nodo y aristas | Lógica |
| Los carriles deben ser verticales en todo ejercicio | AMBIGUO | Ningún material lo declara universal; solo lo solicita el tipo de ejercicio | Orientación | Confirmar enunciado |

## 6. Stack de tecnologías

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Usuario → frontend → Internet → nube → backend/base de datos | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 35; PPTX, diap. 8 | Componentes y enlaces | Flujo arquitectónico |
| Explicación robusta del conjunto y de cada tecnología | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 35 | Secciones por tecnología | Justificación |
| Azure, NGINX, React, Node/Express, SQL y analítica | EJEMPLO_ACADEMICO | `12-StackDeTecnologias.png`, imagen completa | Etiquetas | No copiar marcas sin necesidad |
| Asociar tecnologías con RF/RNF, interfaces, seguridad y capacidad | TECNICO_COMPLEMENTARIO | Sin regla literal | Referencias cruzadas | Viabilidad |

## 7. Diagrama entidad–relación

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Mínimo 40 tablas en DERCAS | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 37; PPTX, diap. 8 | Conteo | Pertinencia |
| Tablas correctamente distribuidas por proceso | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 37 | Trazas proceso–tabla | Distribución conceptual |
| Entidades, atributos, PK, relaciones y cardinalidades | TECNICO_COMPLEMENTARIO | Sin definición literal en el material | Presencia y referencias | Modelo del dominio |
| Resolver M:N y evitar redundancia injustificada | TECNICO_COMPLEMENTARIO | Convención relacional | Relaciones y claves | Normalización |

## 8. Diccionario de datos

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Resumen con cantidad de tablas, campos, PK y FK | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 38; PPTX, diap. 8 | Recalcular conteos | Coherencia |
| Enlace al diccionario completo en anexos | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 53 | Enlace resoluble | Accesibilidad |
| Nombre, definición, tipo, longitud, dominio, nulabilidad y origen | TECNICO_COMPLEMENTARIO | Sin lista literal | Columnas y tipos | Significado |
| El resumen sustituye al diccionario completo | AMBIGUO | Líneas 38 y 53 distinguen resumen y enlace completo | No | Deben conservarse ambos |

## 9. Prototipo

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Pantallas principales con descripción | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 36; PPTX, diap. 8 | Conteo/descripciones | Cobertura |
| La lógica no se revisa en esa sección | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 36 | No | Alcance de la evaluación |
| Enlace al prototipo completo en anexos | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 54 | Enlace | Acceso |
| Trazar pantalla a actor, requisito, datos, estados y validaciones | TECNICO_COMPLEMENTARIO | Sin regla literal | IDs/enlaces | Usabilidad y coherencia |
| Fidelidad y herramienta obligatorias | AMBIGUO | No se especifican | No | Determinar por enunciado |

## 10. DFD de contexto

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Entidades de entrada/salida y proceso central número 0 con nombre del sistema | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 33; PPTX, diap. 8 | Conteo, número y etiquetas | Frontera correcta |
| Candidato, Cliente, Técnico, Personal de mantenimiento y Coordinador con flujos rotulados | EJEMPLO_ACADEMICO | `14-DFDContexto.png`, imagen completa | Etiquetas | Pertinencia al dominio |
| Un solo proceso y ausencia de almacenes internos | TECNICO_COMPLEMENTARIO | Convención DFD de contexto | Conteo/tipos | Nivel de abstracción |
| Balancear los flujos externos con nivel cero | TECNICO_COMPLEMENTARIO | Convención DFD | Comparación de conjuntos | Equivalencia semántica |
| Los dos rectángulos “Cliente” son la misma entidad duplicada para diseño | INFERENCIA | PNG 14, imagen completa; no hay leyenda | Detectar nombre repetido | Confirmar interpretación |

## 11. DFD nivel cero

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Entidades participantes y 2–3 pasos principales de cada proceso | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 34 | Conteos | Selección de procesos |
| Todos los flujos nombrados | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 34 | Etiquetas vacías | Significado |
| Al menos un almacén conectado por proceso | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 34 | Grado de conexión | Pertinencia del almacén |
| Todo proceso tiene entrada y salida | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 34 | Grados | Semántica |
| Procesos 1–11, almacenes D1/D2/D4/D6/D7/D9/D10/D12 y entidades duplicadas por diseño | EJEMPLO_ACADEMICO | `17-DiagramaDFDNivel0.png`, imagen completa | Inventario | Legibilidad y corrección |
| Balance con el contexto y prohibición entidad–almacén directa | TECNICO_COMPLEMENTARIO | Convención DFD | Comparación/aristas | Balance semántico |

## 12. UML casos de uso

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Diagrama general: ingreso al sistema y módulos visitables | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 43 | Login/módulos | Alcance |
| Un caso de uso por cada diagrama de flujo | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 43 | Conteo cruzado | Correspondencia |
| PNG 11 usa `«extends»` desde login hacia módulos; PNG 12 usa `«include»` hacia subcasos y `«extend»` hacia el caso base | EJEMPLO_ACADEMICO | PNG 11 y PNG 12, imagen completa | Dirección/etiquetas | Comparar con intención |
| Actores externos, límite del sistema y semántica UML estándar de include/extend | TECNICO_COMPLEMENTARIO | Convención UML; véase `uml/casos-uso-notacion.md` | Tipos y flechas | Valor observable |

## 13. UML clases

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Mapeo exacto con el diagrama ER en DERCAS | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 44 | Comparar nombres/relaciones | Significado de “exacto” |
| Clases, atributos, operaciones, asociaciones y multiplicidades | TECNICO_COMPLEMENTARIO | Convención UML | Elementos | Responsabilidades |
| Copiar literalmente cada tabla como clase | AMBIGUO | “Mapeo exacto” no define transformación | Comparación parcial | Aclaración docente |
| Existe ejemplo académico original de clases | AMBIGUO | No se suministró uno entre los 22 originales | Inventario | No aplica |

## 14. UML secuencia

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Un diagrama por cada diagrama de flujo | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 45 | Conteo cruzado | Cobertura |
| Líneas de vida, mensajes y orden vertical | EJEMPLO_ACADEMICO | PNG 15 (mitad superior) y PNG 19, imagen completa | Participantes/mensajes | Escenario y orden |
| Activaciones, respuestas, condiciones y fragmentos cuando correspondan | TECNICO_COMPLEMENTARIO | Convención UML | Elementos | Pertinencia |
| Debe representar el mismo escenario que colaboración | INFERENCIA | La fuente exige ambos por flujo, líneas 45–46 | Comparar vocabulario | Equivalencia semántica |

## 15. UML colaboración

| Criterio | Clasificación | Referencia exacta | Automático | Revisión humana |
|---|---|---|---|---|
| Un diagrama por cada diagrama de flujo | ACADEMICO_EXPLICITO | Instrucciones DERCAS, línea 46 | Conteo cruzado | Cobertura |
| Participantes enlazados con mensajes rotulados | EJEMPLO_ACADEMICO | PNG 15, mitad inferior | Participantes/enlaces | Interacción |
| Numeración de mensajes para expresar orden | TECNICO_COMPLEMENTARIO | Convención UML de comunicación; el PNG 15 no muestra numeración legible | Patrón numérico | Orden |
| Equivalencia con el diagrama de secuencia del mismo flujo | INFERENCIA | Exigencia conjunta por flujo, líneas 45–46; ejemplo conjunto PNG 15 | Comparar conjuntos | Equivalencia semántica |

## Decisiones transversales

1. Los mínimos de 40 tablas y 45 actividades son requisitos del DERCAS, no reglas universales.
2. Los PNG son ejemplos académicos; una característica visual aislada no crea obligación.
3. La validación automática solo detecta condiciones observables. La corrección conceptual, pertinencia y legibilidad necesitan revisión humana.
4. “UML de Contexto” permanece `AMBIGUO`; véase `../uml/uml-de-contexto.md`.
