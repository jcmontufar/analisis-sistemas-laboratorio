# Arquitectura, stack y despliegue

## Definición y objetivo

La arquitectura asigna responsabilidades e interfaces; el stack selecciona tecnologías; el despliegue ubica artefactos en nodos y rutas de comunicación. Juntos explican cómo opera la solución.

## Reglas académicas explícitas

DERCAS propone el recorrido usuario → frontend → internet → nube → backend/base de datos y exige explicación robusta del conjunto y de cada tecnología; el despliegue debe basarse en ese stack. Fuente: instrucciones DERCAS, secciones “Stack” y “Anexos”; PPTX, diap. 8.

## Ejemplos, convenciones y vacíos

`12-StackDeTecnologias.png` muestra cliente, Wi-Fi/Internet, NGINX/React, Azure VM, Node/Express, SQL y analítica; `13-DiagramaUMLDespliegue.png` traduce nodos, artefactos, HTTPS/API y conexión SQL. Complemento: justificar cada tecnología por requisito y no confundir marcas con arquitectura. No hay criterios de capacidad, disponibilidad o costos; deben derivarse de RNF/factibilidad.

