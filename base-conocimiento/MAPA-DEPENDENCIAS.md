# Mapa de dependencias entre artefactos

El mapa indica insumos mínimos y comprobaciones cruzadas; no obliga a producir todos los artefactos en cada ejercicio.

```text
Enunciado + fuentes académicas
  └─> Ingeniería de requerimientos
        ├─> Procesos
        │     ├─> Listado de pasos
        │     │     └─> Diagrama de flujo
        │     ├─> DFD de contexto
        │     │     └─> DFD nivel cero
        │     ├─> UML secuencia
        │     │     └─> UML colaboración
        │     └─> Datos identificados
        │           └─> ER
        │                 ├─> Diccionario de datos
        │                 └─> UML clases, si se solicita mapeo
        ├─> Casos de uso <─ Procesos
        └─> Prototipo

Requerimientos no funcionales + restricciones
  └─> Stack de tecnologías
        └─> UML despliegue
```

## Controles de consistencia

| Origen | Destino | Qué debe conservarse |
|---|---|---|
| Requerimiento | Proceso/caso de uso | objetivo, actor y resultado |
| Proceso | Pasos/flujo | actividades, decisiones, responsables, entradas y salidas |
| DFD contexto | DFD nivel cero | entidades y flujos externos balanceados |
| Proceso/requerimiento | Caso de uso | actor, valor observable y alcance |
| Datos del proceso | ER/diccionario | nombre, significado, claves y relaciones |
| ER | UML clases | correspondencia definida por el enunciado; no asumir copia literal |
| Proceso | Secuencia/colaboración | participantes, mensajes, condiciones y resultado |
| Stack | Despliegue | tecnologías, nodos, artefactos y comunicaciones |
| Requerimiento | Prototipo | actor, datos, acción, validación y estado |

Una modificación en un artefacto origen obliga a revisar sus dependientes antes de declarar consistencia.

