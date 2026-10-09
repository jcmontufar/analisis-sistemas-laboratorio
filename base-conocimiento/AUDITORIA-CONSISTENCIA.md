# Auditoría de consistencia

Fecha: 8 de octubre de 2026. Alcance: `base-conocimiento/`, índice de materiales, consultas de recuperación, matrices y `AGENTS.md`.

| ID | Hallazgo | Ubicación | Severidad | Explicación y corrección recomendada | Acción |
|---|---|---|---|---|---|
| AC-01 | Matriz sin clasificación criterio por criterio | `criterios-evaluacion/README.md` anterior | Alta | Mezclaba “académico” y “técnico” en celdas agregadas. Separar 15 matrices y usar las cinco categorías obligatorias. | Aplicada |
| AC-02 | Riesgo de universalizar mínimos DERCAS | ER, cronograma y `AGENTS.md` | Alta | 40 tablas y 45 actividades pertenecen al proyecto DERCAS. Crear regla de alcance explícita. | Aplicada en `DERCAS-vs-EJERCICIOS.md` y `AGENTS.md` |
| AC-03 | Ejemplo PNG 11 tratado como “uso dudoso” sin dictamen | Índice y UML casos de uso | Alta | Auditar rótulo, dirección y diferencia con UML formal. | Aplicada en `uml/casos-uso-notacion.md` |
| AC-04 | “Cliente” duplicado sin clasificación | PNG 14, índice y DFD | Media | Es probablemente la misma entidad repetida por diseño, pero no hay leyenda. Clasificar como inferencia, no regla. | Aplicada |
| AC-05 | Se podía inferir balance entre ejemplos DFD incompatibles | PNG 14 y PNG 17 | Alta | Contexto = servicios de drenajes; nivel cero = clínica dental. No forman un par validable. | Aplicada; balance marcado no evaluable |
| AC-06 | “UML de Contexto” interpretado como no estándar sin agotar evidencia | UML y matrices | Alta | Conservar texto literal, buscar definición y clasificar `AMBIGUO`. | Aplicada en `uml/uml-de-contexto.md` |
| AC-07 | “Mapeo exacto” ER–clases podía entenderse como copia literal | UML clases | Media | La fuente no define la transformación. Mantener la exigencia y pedir aclaración del significado. | Aplicada en matriz 13 |
| AC-08 | Informe final y manuales podían presentarse como exigencia absoluta | Resumen DERCAS | Media | La fuente introduce esos productos con “se recomienda”. Preservar el matiz. | Aplicada en `DERCAS-vs-EJERCICIOS.md` |
| AC-09 | Terminología “colaboración” y “comunicación” no normalizada | Fichas UML | Baja | Usar “colaboración (comunicación)” y explicar que es la vista de interacción centrada en vínculos. | Aplicada en matrices/mapa; pendiente renombrar archivos no necesario |
| AC-10 | Referencias genéricas “instrucciones DERCAS” | Varias fichas de base | Media | Para evaluación, citar línea; para síntesis, mantener sección y remitir a matriz auditada. | Aplicada en matrices; fichas conservan referencias temáticas válidas |
| AC-11 | Flujo con carriles verticales podía parecer regla universal | Matriz de flujo | Media | El material muestra carriles, pero no exige orientación universal. | Aplicada: `AMBIGUO` salvo enunciado |
| AC-12 | Reglas técnicas presentadas junto a fuente académica sin tipo visible | DFD/UML/factibilidad | Media | Separar reglas explícitas, ejemplos e incorporación técnica. | Aplicada mediante matrices y documentos de auditoría |
| AC-13 | Rótulos pequeños del DFD nivel cero podían transcribirse con exceso de confianza | PNG 17 | Media | Marcar lo no legible y no inventar. | Aplicada con `[REQUIERE_REVISION_VISUAL]` |
| AC-14 | No existía mapa para detectar propagación de cambios | Base completa | Media | Definir dependencias y controles cruzados. | Aplicada en `MAPA-DEPENDENCIAS.md` |

## Contradicciones conservadas

- El PNG 11 usa `<<extends>>` para conectar login con módulos; el PNG 12 representa `include/extend` de manera compatible con UML estándar. Ambos se conservan como ejemplos, no como una regla única.
- El requisito DERCAS “un almacén por proceso” se conserva como `ACADEMICO_EXPLICITO`, aunque no es una regla DFD universal.
- “UML de Contexto” sigue sin definición suficiente.

## Pendientes que requieren autoridad docente

1. Qué artefacto significa “UML de Contexto”.
2. Si “mapeo exacto” ER–clases exige equivalencia uno a uno o solo trazabilidad.
3. Si informe final y manuales son obligatorios en una entrega concreta.
4. Qué notación DFD formal debe usarse cuando el enunciado no la indica.

