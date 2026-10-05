# UML integrado

## Objetivo y elementos

UML ofrece vistas complementarias: casos de uso (valor externo), clases (estructura), secuencia/colaboración (interacción), actividades (flujo), estados (ciclo de vida), componentes (dependencias) y despliegue (nodos/artefactos).

## Reglas académicas explícitas

DERCAS exige caso de uso general tras login y uno por flujo; clases en correspondencia exacta con ER; secuencia y colaboración por flujo; componentes de todos los módulos; despliegue basado en stack; estados por flujo. Fuente: `11-InstruccionesDeRevisionDERCAS.md`, sección “Anexos”; PPTX, diap. 10.

## Convenciones complementarias

- Casos: actores externos, límite; `include` apunta al comportamiento obligatorio reutilizado y `extend` al caso base opcional.
- Clases: atributos/operaciones, asociaciones y multiplicidades; no confundir con tablas.
- Secuencia y colaboración: mismos participantes, mensajes, orden, condiciones y resultado.
- Actividades: inicio/fin, acciones, decisiones y carriles; estados: estados, eventos/guardas y transiciones.
- Despliegue: nodos, entornos, artefactos y protocolos coherentes con el stack.

## Ejemplos y vacíos

Ejemplos: PNG 11/12 (casos), 15/19 (interacciones), 16 (actividad), 18 (estados), 13 (despliegue). El PNG 11 usa `extend` como enlace a módulos y no debe copiarse sin revisar. Falta un ejemplo académico de clases/componentes. “UML de Contexto” es ambiguo y requiere aclaración docente.

