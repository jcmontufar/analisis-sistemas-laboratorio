# Instrucciones para agentes

## Alcance

Este repositorio es un laboratorio académico de análisis y diseño de sistemas. No es una aplicación empresarial. Todos los entregables deben redactarse en español y conservar una fuente editable junto a cada exportación.

## Flujo obligatorio

1. Leer primero el enunciado original del ejercicio y registrar sus entregables.
2. Identificar las fuentes académicas pertinentes mediante `material-didactico/indice.md`; citar archivo y página, diapositiva o sección.
3. Consultar las reglas y matrices pertinentes de `base-conocimiento/`.
4. Separar reglas explícitas del catedrático de convenciones técnicas complementarias.
5. Elaborar el análisis lógico en `analisis.md` antes de dibujar; registrar datos faltantes y suposiciones mínimas sin inventar información que cambie la solución.
6. Mantener coherencia de nombres, actores, procesos, datos y relaciones entre artefactos.
7. Generar y conservar la fuente editable en `diagramas/fuentes/`.
8. Exportar diagramas completos y legibles a SVG y PNG en `diagramas/exportados/`, cuando corresponda.
9. Verificar sintaxis, estructura, referencias cruzadas y, en proporción al riesgo, el renderizado.
10. Registrar en `validacion.md` qué se comprobó automáticamente, qué requiere revisión humana y toda limitación.
11. Conservar en la carpeta del ejercicio el enunciado, análisis, solución, validación, fuentes, exportaciones y documentos.
12. Ejecutar `python scripts/validacion/validar_proyecto.py` antes de entregar.

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
- Las convenciones técnicas complementarias llenan vacíos sin atribuirse al catedrático.
- Un PNG de ejemplo puede contener defectos: no convertir su apariencia en regla sin respaldo textual.
- Ante una contradicción material, documentarla y solicitar criterio; no alterar originales ni ocultar la diferencia.

## Seguridad y Git

- Nunca almacenar contraseñas, tokens, credenciales ni material académico en repositorios públicos.
- Verificar `git status` y la privacidad del remoto antes de publicar.
- Usar una rama de trabajo para cambios significativos.
