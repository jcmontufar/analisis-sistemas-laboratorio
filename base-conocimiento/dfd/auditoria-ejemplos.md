# Auditoría de los ejemplos DFD

## DFD de contexto: cliente duplicado

Fuente: `material-didactico/originales/14-DFDContexto.png`.

El nombre exacto “Cliente” aparece en dos rectángulos: a la izquierda envía solicitud, emergencia, evidencia y confirmación/observaciones; a la derecha recibe cotización, cambios, reporte y estimación. No hay calificadores que indiquen dos roles conceptualmente distintos.

**Conclusión:** la explicación más probable es una duplicación visual intencional de la misma entidad para reducir cruces. Es una `INFERENCIA` de certeza media-alta, porque el diagrama no incluye leyenda de duplicación. No es una regla de modelado ni evidencia suficiente para inventar dos tipos de cliente.

## DFD nivel cero

Fuente: `material-didactico/originales/17-DiagramaDFDNivel0.png`.

### Elementos legibles

- Entidades externas: Asistente dental, Pacientes (repetido visualmente), Odontólogo y Administrador.
- Procesos: 1 Gestionar pacientes; 2 Gestionar agenda y citas; 3 Gestionar expediente clínico; 4 Gestionar tratamientos; 5 Gestionar odontograma; 6 Gestionar procedimientos e insumos clínicos; 7 Gestionar medicamentos y recetas; 8 Generar comprobantes; 9 Gestionar notificaciones; 10 Gestionar contacto web; 11 Gestionar usuarios y roles.
- Almacenes: D1 Pacientes, D2 Citas, D4 Comprobantes, D6 Odontograma, D7 Historial clínico, D9 Procedimientos e insumos, D10 Medicamentos y recetas y D12 Mensajes/contacto.
- La numeración de procesos es continua 1–11; la numeración de almacenes tiene saltos, lo que no es por sí mismo un error.
- Se observan entradas y salidas en los once procesos y los flujos visibles están rotulados.

### Rótulos que no deben transcribirse sin ampliación adicional

- Flujo superior entre Asistente dental y proceso 2: `[REQUIERE_REVISION_VISUAL]`.
- Algunos retornos entre procesos 3–7 y sus almacenes: `[REQUIERE_REVISION_VISUAL]`.
- Flujos largos inferiores hacia proceso 11: `[REQUIERE_REVISION_VISUAL]`.

### Correspondencia con contexto

No puede comprobarse balance con `14-DFDContexto.png`: ese contexto describe servicios industriales de drenajes, mientras que el nivel cero describe una clínica dental (SIGAMED). Son ejemplos de dominios distintos. Por tanto, cualquier afirmación de correspondencia sería falsa; para validar balance se necesita el contexto del sistema SIGAMED.

## Clasificación

- Rasgos visibles del PNG: `EJEMPLO_ACADEMICO`.
- Balance, prohibición de entidad–almacén directa y unicidad conceptual de entidades duplicadas: `TECNICO_COMPLEMENTARIO`.
- Intención de las duplicaciones: `INFERENCIA`.
- Balance entre PNG 14 y PNG 17: `AMBIGUO`/no evaluable por falta del par correcto.

