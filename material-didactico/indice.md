# Índice del material didáctico

Inventario verificado el 4 de octubre de 2026. Los 22 archivos se conservaron sin modificación en `originales/`; sus SHA-256 constan en `manifiesto-sha256.txt`. No se detectaron duplicados, corrupción ni archivos ilegibles. Los dos PDF y el PPTX son imágenes sin texto nativo: su contenido se revisó visualmente y se resumió en `extraidos/`.

| Archivo | Formato | Tema principal | Estado y referencia útil |
|---|---|---|---|
| `01-El_Camino_a_la_Sabiduría.png` | PNG | Datos, información, conocimiento y sabiduría | Legible; imagen completa |
| `02-Systems_Architecture_Foundations.pdf` | PDF, 15 págs. | Sistemas, SDLC, cascada, incremental y RUP | Legible, sin texto nativo; págs. 1–15 |
| `03-Ciclo_de_Vida_del_Software.png` | PNG | Siete fases del ciclo de vida | Legible; imagen completa |
| `04-Pirámide_de_sistemas_de_información.png` | PNG | TPS, KWS/OAS, MIS/DSS y ESS | Legible; imagen completa |
| `05-Requirements_Engineering.pdf` | PDF, 15 págs. | Elicitación, RF/RNF, trazabilidad y procesos | Legible, sin texto nativo; págs. 1–15 |
| `06-EntrevistaInicial.png` | PNG | Formato de entrevista institucional | Legible; imagen completa |
| `07-EntrevistaPorProceso.png` | PNG | Formato de entrevista por proceso | Legible; imagen completa |
| `08-TablaDeRequerimientos.png` | PNG | Ejemplo de tabla RF/RNF | Legible; imagen completa |
| `09-DescripcionDelProceso.png` | PNG | Descripción narrativa de procesos | Legible; imagen completa |
| `10-DescripcionProceso.png` | PNG | Listado jerárquico de pasos y responsables | Legible; imagen completa |
| `11-CasosDeUsoAccesoAlSistema.png` | PNG | Acceso y módulos en casos de uso | Legible; revisar semántica de `extend` |
| `11-InstruccionesDeRevisionDERCAS.md` | Markdown | Rúbrica detallada DERCAS | Texto UTF-8 legible; secciones temáticas |
| `11-The_DERCAS_Software.pptx` | PPTX, 11 diap. | Síntesis de entregables DERCAS | Legible, sin texto nativo; diap. 1–11 |
| `12-CasosDeUsoProceso.png` | PNG | Caso de uso por rol/proceso | Legible; revisar direcciones `include/extend` |
| `12-StackDeTecnologias.png` | PNG | Arquitectura Azure, frontend, backend y datos | Legible; imagen completa |
| `13-DiagramaUMLDespliegue.png` | PNG | Nodos, artefactos y comunicaciones | Legible; imagen completa |
| `14-DFDContexto.png` | PNG | Proceso 0, entidades y flujos | Legible; “Cliente” aparece dos veces |
| `15-DiagramaUMLSecuenciaColaboracion.png` | PNG | Secuencia y colaboración equivalentes | Legible; imagen completa |
| `16-DiagramaDeActividades.png` | PNG | Actividades con carriles | Legible; imagen completa |
| `17-DiagramaDFDNivel0.png` | PNG | Procesos, entidades, almacenes y flujos | Legible; rótulos densos, revisión humana recomendada |
| `18-DiagramaEstados.png` | PNG | Estados de tratamientos/odontograma | Legible; revisar eventos/guardas |
| `19-DiagramaSecuencia.png` | PNG | Secuencia de contratación y permisos | Legible; 27 mensajes |

## Procedencia y método

Los archivos aparecieron inicialmente en la raíz del proyecto, aunque el encargo indicaba que estaban en `originales/`. Se trasladaron únicamente los 22 nombres numerados, comprobando SHA-256 antes y después. No existía un manifiesto externo; `manifiesto-sha256.txt` establece la línea base del repositorio.

## Convención de uso

- Una regla se marca **académica explícita** solo si aparece en el material y se cita con página, diapositiva o sección.
- Un ejemplo visual no constituye por sí solo una regla y puede contener defectos.
- Las reglas UML/DFD añadidas para consistencia se marcan **convención técnica complementaria**.
- Los detalles pequeños de materiales rasterizados requieren validación humana cuando una entrega dependa literalmente de un rótulo.
