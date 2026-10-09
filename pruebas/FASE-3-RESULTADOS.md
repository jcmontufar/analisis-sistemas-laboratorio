# Informe de auditoría académica y normalización

Fecha: 8 de octubre de 2026.

## Matrices auditadas

Se auditaron las 15 matrices solicitadas. La tabla agregada anterior fue sustituida por 15 secciones independientes con 65 criterios:

| Clasificación | Criterios |
|---|---:|
| `ACADEMICO_EXPLICITO` | 30 |
| `EJEMPLO_ACADEMICO` | 9 |
| `TECNICO_COMPLEMENTARIO` | 17 |
| `INFERENCIA` | 3 |
| `AMBIGUO` | 6 |

Cada criterio conserva fuente, validación automática posible y revisión humana.

## Contradicciones y ambigüedades

- PNG 11 usa `<<extends>>` desde login hacia módulos; difiere en rótulo y finalidad de UML formal. PNG 12 sí muestra direcciones compatibles con UML estándar.
- “Cliente” repetido en PNG 14 es probablemente la misma entidad duplicada por diseño; se conserva como `INFERENCIA`.
- PNG 14 y PNG 17 no pueden balancearse: describen servicios industriales de drenajes y una clínica dental, respectivamente.
- “UML de Contexto” permanece `AMBIGUO`: la fuente lo exige, pero no lo define ni ejemplifica.
- “Mapeo exacto” ER–clases no determina si debe existir equivalencia uno a uno.
- Informe final y manuales aparecen bajo “se recomienda”; su obligatoriedad depende del enunciado.
- Los rótulos pequeños identificados en PNG 17 quedaron marcados `[REQUIERE_REVISION_VISUAL]`.

Los 14 hallazgos, su severidad y acciones se registraron en `base-conocimiento/AUDITORIA-CONSISTENCIA.md`.

## Cambios aplicados

- Separación explícita entre DERCAS y ejercicios individuales.
- Dictámenes de casos de uso, DFD y “UML de Contexto”.
- Mapa de dependencias y controles cruzados.
- Checklist de prevalidación.
- Plantilla maestra de seis documentos para ejercicios.
- Generador de ejercicios conectado a la plantilla maestra.
- `AGENTS.md` normalizado al flujo obligatorio de 12 pasos.
- Validador ampliado para plantilla y simulación.

## Simulación

`pruebas/caso-tecnico/` contiene el caso inventado `CASO_TECNICO_DE_PRUEBA`: “Una biblioteca registra préstamos de libros”.

- carpeta aislada fuera de `ejercicios/`;
- fuentes seleccionadas;
- actor supuesto identificado como suposición;
- proceso, entrada, salida y datos mínimos registrados;
- fuente PlantUML editable;
- SVG y PNG generados;
- sintaxis validada;
- PNG revisado visualmente y legible;
- checklist ejecutado.

La simulación demuestra funcionamiento técnico, no corrección académica.

## Validaciones ejecutadas

| Validación | Resultado |
|---|---|
| Material didáctico | 22/22; 0 errores, 0 duplicados |
| Proyecto y enlaces | 0 errores, 0 avisos |
| Formatos MD/CSV/DOCX/XLSX/PDF/PNG/SVG | Éxito |
| PlantUML | SVG y PNG generados |
| Mermaid | SVG generado |
| draw.io | XML editable generado |
| DBML | SQL PostgreSQL generado |
| DOT | SVG generado |
| Credenciales | Sin coincidencias |
| npm | 5 vulnerabilidades bajas transitivas; 0 moderadas o superiores |

## Publicación

- Commit de implementación publicado: `1c462bba001268851cafcfc9f5568ddac13ef71a`.
- Rama publicada: `main`.
- Repositorio comprobado mediante GitHub CLI: `PRIVATE`, rama predeterminada `main`.
- Este informe se incorpora en un commit de documentación posterior; el SHA final de `HEAD`, `origin/main` y GitHub se comprueba después de publicarlo.
