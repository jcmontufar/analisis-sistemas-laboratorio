# Instrucciones para agentes

## Alcance

Este repositorio es un laboratorio académico de análisis y diseño de sistemas. No es una aplicación empresarial. Todos los entregables deben redactarse en español y conservar una fuente editable junto a cada exportación.

## Flujo obligatorio

1. Leer el enunciado original y conservarlo sin reinterpretar.
2. Identificar el tipo de artefacto solicitado.
3. Consultar su matriz en `base-conocimiento/criterios-evaluacion/README.md`.
4. Consultar las fuentes académicas pertinentes mediante `material-didactico/indice.md`.
5. Diferenciar `ACADEMICO_EXPLICITO`, `EJEMPLO_ACADEMICO`, `TECNICO_COMPLEMENTARIO`, `INFERENCIA` y `AMBIGUO`.
6. Detectar y registrar ambigüedades y datos faltantes.
7. Analizar el problema antes de dibujar, usando `plantillas/VALIDACION-EJERCICIO.md`.
8. Generar y conservar la fuente editable en `diagramas/fuentes/`.
9. Renderizar SVG y PNG completos y legibles en `diagramas/exportados/`, cuando corresponda.
10. Validar sintaxis, estructura, referencias y renderizado sin confundirlos con corrección académica.
11. Revisar consistencia con artefactos dependientes mediante `base-conocimiento/MAPA-DEPENDENCIAS.md`.
12. Documentar cada suposición en `suposiciones.md` y las limitaciones en `validacion.md`.

Está prohibido generar directamente un diagrama sin análisis previo.

## Reglas generales de modelado

- Resolver exactamente el problema solicitado y respetar instrucciones particulares.
- Usar notación técnica correcta, priorizando claridad visual y legibilidad.
- Exportar sin cortes, con etiquetas legibles y tamaño apropiado.
- No declarar corrección académica solo porque un archivo se renderiza.
- No sobrescribir soluciones aprobadas ni eliminar originales sin autorización.

## DFD

- Aplicar Kendall y Kendall cuando el ejercicio lo indique.
- Contexto: representar el sistema como un único proceso, usar número 0 cuando corresponda, identificar entidades externas y nombrar y orientar todos los flujos.
- Nivel cero: descomponer procesos principales, incluir almacenes pertinentes y mantener el balance de flujos externos con el contexto.
- Evitar procesos sin entrada o salida y conexiones directas inválidas entre entidad externa y almacén.

## UML

### Casos de uso

- Identificar actores y ubicar casos dentro del límite del sistema.
- Usar `«include»` para comportamiento obligatorio reutilizado y `«extend»` para comportamiento opcional condicionado, verificando la dirección de la dependencia.
- No usar relaciones UML solo para representar navegación entre pantallas.

### Clases

- Incluir clases relevantes, atributos y operaciones pertinentes, asociaciones y multiplicidades.
- Usar herencia, agregación o composición únicamente con justificación.
- Distinguir un modelo de dominio UML de un modelo relacional.

### Secuencia y comunicación

- Identificar participantes, mensajes, orden temporal, respuestas y condiciones aplicables.
- Mantener equivalencia semántica entre diagramas de secuencia y comunicación.

## Flujo y procesos

- Incluir inicio, fin, operaciones, decisiones y caminos alternativos requeridos.
- Usar carriles cuando sea necesario identificar responsables.

## Entidad-relación

- Identificar entidades, atributos, claves, cardinalidades y relaciones documentadas.
- Evitar redundancias injustificadas.
- No imponer cantidades mínimas de tablas salvo exigencia expresa del enunciado. En DERCAS sí rige el mínimo académico de 40 tablas.

## Jerarquía de evidencia

- El enunciado particular gobierna el ejercicio.
- Después se aplican las exigencias académicas citadas en la base de conocimiento.
- Los requisitos DERCAS solo rigen un ejercicio individual cuando el enunciado los incorpora.
- Las convenciones técnicas complementarias llenan vacíos sin atribuirse al catedrático.
- Un PNG de ejemplo puede contener defectos: no convertir su apariencia en regla sin respaldo textual.
- Ante una contradicción material, documentarla y solicitar criterio; no alterar originales ni ocultar la diferencia.
- “UML de Contexto” permanece ambiguo y no se sustituye automáticamente por otro artefacto.

## Seguridad y Git

- Nunca almacenar contraseñas, tokens, credenciales ni material académico en repositorios públicos.
- Verificar `git status` y la privacidad del remoto antes de publicar.
- Usar una rama de trabajo para cambios significativos.
