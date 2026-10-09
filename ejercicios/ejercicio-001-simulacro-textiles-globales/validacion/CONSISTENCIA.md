# Consistencia cruzada

| Elemento | DFD Contexto | DFD 0 | Casos de Uso | Secuencia | Colaboración |
|---|---|---|---|---|---|
| Jefe de Planta | F01/F02 | P1, D1 | Crear OT; verificar metraje | 1–4 | 1–4 |
| Operario de Corte | F03/F04 | P2, D2 | Registrar corte; conteo y merma | 5–8 | 5–8 |
| Operario de Confección | F05/F06 | P3, D3 | Registrar confección; avance y tiempo | 9–12 | 9–12 |
| Inspector de Calidad | F07/F08 | P4, D4 | Inspección; rechazo; Liberar aprobadas para empaque | 13–20 | 13–20 |
| OT y tela | F01/F02 | P1→P2, D1 | Crear OT incluye verificar metraje | 1–4 | 1–4 |
| Corte y paquetes | F03/F04 | P2→P3, D2 | Conteo y merma obligatorios | 5–8 | 5–8 |
| Avance y duración | F05/F06 | P3→P4, D3 | Avance y tiempo obligatorios | 9–12 | 9–12 |
| Aprobada/rechazada | Resultado y resumen F07/F08 | P4, D4 | Rechazo extiende inspección | loop 13–17; alt 14/15 | 13–17; guardas 14/15 |
| Código de lote | F08 | P4→D4; D4→P1 para F02 | Liberar aprobadas para empaque incluye Generar código de lote | 18–20 tras calidad; 20 confirma liberación | 18–20 idénticos; 20 confirma liberación |
| Persistencia | Oculta por nivel de abstracción | D1–D4 | No es actor humano | Participante técnico PostgreSQL | Mismo participante técnico |

F04: Datos de corte y estado del registro.

F06: Datos de paquete habilitado y estado de confección.

Mensaje 20: Código de lote y confirmación de liberación.

Los mensajes son un escenario representativo, no el catálogo completo de consultas del sistema. P4 actualiza D4; P1 consulta D4 para producir el resumen F02 al Jefe. D4 repetido junto a P1 representa el mismo almacén lógico, no un quinto almacén. Los datos de corte y paquetes tienen soporte en los almacenes y no necesitan una segunda secuencia independiente. Las confirmaciones, el ID interno, la liberación solo de aprobadas y el stack son inferencias/decisiones técnicas registradas; no se atribuyen al PDF. El Inspector libera aprobadas y genera el lote; no se le atribuye el empaque físico.

Los 20 identificadores, emisores, receptores y contenidos se comparan automáticamente entre secuencia y colaboración. Los ocho flujos se comparan normalizando únicamente espacios y saltos visuales de línea.
