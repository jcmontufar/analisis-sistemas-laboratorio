# Análisis verificado del caso

Fuente primaria: Simulacro de examen .pdf, pp. 1–2. Leído completo y revisado visualmente. El texto recibido complementa entregables.

## Problema y objetivo
La gestión mediante papel y controles verbales produce retrasos, pérdida de información y falta de trazabilidad (p. 1). Se propone registrar la manufactura desde habilitación y corte hasta liberación y empaque. Solo producción; no se agregan compras, ventas, RRHH ni inventario comercial.

## Actores y procesos
| ID | Actor | Proceso | Entradas | Salidas |
|---|---|---|---|---|
| P1 | Jefe de Planta | 1.0 Gestionar Orden de Producción | Orden de Trabajo y datos de tela asignada | OT habilitada y resumen de producción |
| P2 | Operario de Corte | 2.0 Gestionar Corte | Registro de corte y merma | Datos de corte y estado del registro |
| P3 | Operario de Confección | 3.0 Gestionar Confección | Registro de avance y tiempo por lote | Datos de paquete habilitado y estado de confección |
| P4 | Inspector de Calidad | 4.0 Gestionar Calidad y Empaque | Resultado de inspección y defectos | Resumen de calidad y código de lote |

Los participantes y procesos son explícitos (pp. 1–2). Los mensajes de salida de coordinación y confirmación son INFERENCIA funcional para que cada usuario conozca el trabajo y confirme su registro. “Resumen de producción” permite al Jefe consultar los controles; no introduce un actor adicional.

## Datos y controles explícitos
OT: modelo, cantidad de prendas, color y tallas; metraje asignado frente al estándar teórico. Corte: conteo obligatorio y porcentaje de merma. Confección: avance por paquete terminado y tiempo por lote. Calidad: inspección individual de acabado/costuras/dimensiones; conteo de aprobadas y rechazadas con causa (mancha, rotura, mala costura). Código de lote para empaque después de calidad.

## Reglas e inferencias
R1: registrar OT y comparación de metraje; sin tolerancia inventada, mostrar diferencia para verificación del Jefe.
R2: contar piezas y cuantificar merma en corte.
R3: registrar paquete terminado y duración por lote.
R4: toda prenda inspeccionada tiene clasificación y las rechazadas tienen causa.
R5: generar código de empaque para prendas aprobadas; mantener rechazadas segregadas y registradas. La liberación exclusiva de aprobadas es INFERENCIA.
R6: ID interno de seguimiento desde OT; código de empaque al liberar. Convención técnica para evitar depender de un código final aún inexistente.
R7: generar un único código de empaque por liberación aprobada y validar unicidad. No inventar una estructura comercial.
R8: no añadir reproceso/descarte sin instrucciones.

## Almacenes justificados
D1 Órdenes de producción y tela: conserva OT, estándar, metraje e ID interno.
D2 Registros de corte: conserva piezas, merma, paquete e ID de OT.
D3 Avances de confección: conserva avance por paquete y duración por lote.
D4 Inspecciones y lotes liberados: conserva criterios, clasificación, defecto y código de empaque. Se unifican calidad y salida final sin un almacén duplicado.
Almacenes son modelado técnico derivado de los datos explícitos. P4 actualiza D4; P1 lee D4 mediante «Resumen de calidad y lote liberado» para elaborar F02, además de consultar D1. Se elimina la transferencia directa P4→P1. La segunda representación de D4 junto a P1 es el mismo almacén lógico, no un quinto almacén ni una copia física.

## Flujos externos balanceados
F01 Jefe → sistema: Orden de Trabajo y datos de tela asignada.
F02 sistema → Jefe: OT habilitada y resumen de producción.
F03 Corte → sistema: Registro de corte y merma.
F04 sistema → Corte: Datos de corte y estado del registro.
F05 Confección → sistema: Registro de avance y tiempo por lote.
F06 sistema → Confección: Datos de paquete habilitado y estado de confección.
F07 Inspector → sistema: Resultado de inspección y defectos.
F08 sistema → Inspector: Resumen de calidad y código de lote.
Los dos DFD conservan exactamente estos ocho intercambios; las actividades físicas se describen en el análisis, no como flujos de datos.

## Casos de uso
Crear OT y habilitar tela incluye Verificar metraje.
Registrar corte incluye Registrar conteo y merma.
Registrar confección incluye Registrar avance y tiempo.
Registrar inspección incluye Clasificar y contar prendas.
Registrar causa de rechazo extiende Registrar inspección cuando [prenda rechazada].
Liberar aprobadas para empaque incluye Generar código de lote. Precondición: existen prendas aprobadas. El Inspector registra la liberación y obtiene el código; no se le atribuye la ejecución del empaque físico. Se mantiene el nombre de P4, Gestionar Calidad y Empaque, como gestión de datos de calidad, liberación y lote.
La relación extend apunta al caso base; include apunta al comportamiento incluido. Los nombres plurales del PDF se normalizan a UML estándar conforme al encargo.

## Escenario de interacción
Cuatro actores, Sistema de Gestión de Manufactura y Persistencia. OT → corte → confección → inspección individual → alternativa aprobada/rechazada → liberación y código de empaque. Secuencia y colaboración reutilizan los mismos 20 mensajes numerados, incluyendo respuestas de persistencia y guardas. Los mensajes 1–19 se mantienen. El 18 corresponde a Liberar aprobadas para empaque; el 20 es «Código de lote y confirmación de liberación»: confirma el registro de liberación, no un empaque físico realizado. En colaboración, llamadas abreviadas numeradas sobre enlaces conservan emisores, receptores y guardas; la tabla inferior conserva los 20 contenidos completos.

## Fórmulas propuestas
Diferencia de tela = metraje asignado - estándar teórico (metros).
Merma propuesta = metros desperdiciados / metros utilizados en corte × 100. Denominador y unidad deben aprobarse; no se resta un conteo de piezas de un metraje.
Duración = fin - inicio del lote, en minutos; tiempos por paquete se agregan sin duplicar intervalos paralelos.
Conteo inspeccionado = aprobadas + rechazadas. Cantidad fabricada y piezas cortadas no son equivalentes sin la composición del modelo.

## Justificación tecnológica previa al stack
Interfaz web con HTML/CSS adaptable y JavaScript mínimo; colores con texto e iconos para evitar depender solo del color. Aplicación monolítica Django que sirve interfaz y API en un servicio administrado; PostgreSQL central, respaldo separado y monitoreo. No se requiere microservicios ni SPA independiente. El diagrama separa responsabilidades frontend/backend, no dos despliegues. Las zonas Planta, Perímetro y Nube agrupan dispositivos/red, router-firewall/Internet y servicio/datos/respaldo respectivamente. HTTPS etiqueta el enlace hacia el servicio, no un componente. Nube condicionada a conectividad y energía verificadas; RPO 24 h y RTO 8 h siguen siendo objetivos propuestos, no garantías.
