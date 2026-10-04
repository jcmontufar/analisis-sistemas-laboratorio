# Instrucciones para agentes

## Alcance

Este repositorio es un laboratorio académico de análisis y diseño de sistemas. No es una aplicación empresarial. Todos los entregables deben redactarse en español y conservar una fuente editable junto a cada exportación.

## Flujo obligatorio

1. Leer el enunciado original del ejercicio.
2. Consultar primero `material-didactico/indice.md` y las referencias pertinentes de `base-conocimiento/`.
3. Separar las reglas explícitas del catedrático de las convenciones técnicas complementarias.
4. Registrar datos faltantes y suposiciones mínimas en `analisis.md`; no inventar información que cambie la solución.
5. Mantener coherencia de nombres, actores, procesos, datos y relaciones entre todos los artefactos.
6. Conservar fuentes editables en `diagramas/fuentes/` y exportaciones completas y legibles en `diagramas/exportados/`.
7. Ejecutar `python scripts/validacion/validar_proyecto.py` y completar la revisión manual de `validacion.md`.

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
- No imponer cantidades mínimas de tablas salvo exigencia expresa del enunciado.

## Seguridad y Git

- Nunca almacenar contraseñas, tokens, credenciales ni material académico en repositorios públicos.
- Verificar `git status` y la privacidad del remoto antes de publicar.
- Usar una rama de trabajo para cambios significativos.
