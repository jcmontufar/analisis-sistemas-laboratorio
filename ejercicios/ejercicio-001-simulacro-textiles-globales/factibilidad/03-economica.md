# Factibilidad económica y modelo parametrizado

El PDF p. 2 permite adquirir equipos y servicios si la inversión se justifica. No proporciona precios, empleados, volumen, salarios, costos de tela ni tasas de merma. Este modelo usa variables de cotización; no son precios del examen ni cotizaciones de mercado.

Moneda: POR DEFINIR. Horizonte comparativo: primer año (supuesto académico). q indica unidades realmente aprobadas y p precio unitario cotizado. No se inventa una estación por empleado.

## A Hardware e infraestructura
| Concepto | Cantidad | Precio de referencia a obtener | Subtotal |
|---|---|---|---|
| Tabletas protegidas o terminales | q_dispositivos | p_dispositivo según alternativa | q_dispositivos × p_dispositivo |
| Equipos administrativos | q_admin | p_admin | q_admin × p_admin |
| Lectores | q_lectores | p_lector | q_lectores × p_lector |
| Impresoras | q_impresoras | p_impresora | q_impresoras × p_impresora |
| AP, switch y cableado | q_AP y puntos medidos | p_AP, p_switch y costo_cableado | q_AP × p_AP + costo_switch + costo_cableado |
| Router y UPS | cantidades según diseño | cotización por carga | costo_router + costo_UPS |
H = suma de subtotales. Etiquetas/consumibles recurrentes van en D. Cantidades pendientes de puestos reales.

## B Servicios y software
| Concepto | Inversión inicial | Costo anual |
|---|---|---|
| Configuración de aplicación y BD | c_configuracion | No duplicar implementación en C |
| Aplicación administrada | c_alta_app | 12 × mensual_app |
| PostgreSQL administrado | c_alta_BD | 12 × mensual_BD |
| Respaldo y monitoreo | c_alta_respaldo | 12 × mensual_respaldo |
| Dominio/certificado | c_alta_dominio | anual_dominio y costo_certificado si procede |
| Licencias del stack abierto | Verificar condiciones de distribución | No implica hosting o soporte gratuito |

B0 = altas/configuración; B_anual = suscripciones. Django/PostgreSQL son elección técnica; no se imputa ficticiamente una licencia comercial.

## C Capacitación e implementación
| Concepto | Base de cálculo | Subtotal |
|---|---|---|
| Jefe | 2 sesiones × 2 h × cohortes_Jefe | 4 × cohortes_Jefe × tarifa_facilitador |
| Corte | 3 sesiones × 2 h × cohortes_Corte | 6 × cohortes_Corte × tarifa_facilitador |
| Confección | 3 sesiones × 2 h × cohortes_Confeccion | 6 × cohortes_Confeccion × tarifa_facilitador |
| Calidad | 3 sesiones × 2 h × cohortes_Calidad | 6 × cohortes_Calidad × tarifa_facilitador |
| Tiempo de asistentes | Horas reales × participantes reales × costo_hora | POR DEFINIR; no duplicar costo facilitador |
| Análisis, configuración funcional, desarrollo, pruebas y puesta en marcha | horas_por_fase × tarifa_por_fase | Suma cotizada |
| Instalación física | Cotización de contratista | No duplicar cableado incluido en H |

C0 = facilitación + oportunidad del personal + implementación + instalación no incluida. Una cohorte por rol supone 22 horas de facilitación; no establece cantidad de trabajadores.

## D Costos operativos anuales
| Concepto | Fórmula |
|---|---|
| Servicios B | B_anual |
| Internet | 12 × mensual_internet |
| Mantenimiento aplicación/equipos | contrato_anual_mantenimiento |
| Electricidad incremental | kWh_medidos × tarifa_kWh |
| Etiquetas y consumibles | unidades_reales × costo_unitario |
| Refuerzos de capacitación | horas_refuerzo × tarifa |
| Reserva para reparación | supuesto aprobado por finanzas |

O_anual = suma de D, incluyendo B_anual una sola vez.
Inversion_inicial I = H + B0 + C0.
Costo_total_primer_año = I + O_anual.
Para comparar local/nube, mantener iguales estaciones, capacitación y funciones; variar servidor, servicios, energía, respaldo y administración.

## Beneficios medibles sin monetización inventada
| Beneficio | Indicador a levantar antes y después |
|---|---|
| Menos merma | Metros desperdiciados/metros utilizados; costo real de tela |
| Menos errores | Registros corregidos y prendas afectadas por errores de información |
| Trazabilidad | Lotes con historial completo y tiempo de búsqueda |
| Medición de tiempos | Duración por lote con carga comparable |
| Menos papel | Hojas y costo real de formularios |
| Disponibilidad de información | Tiempo hasta que Jefe consulta avances |

Menos papel no equivale automáticamente a ahorro de empleados. No atribuir al sistema reducción de defectos de costura sin evidencia.

## Escenarios y umbral
Escenario 0: sin beneficio monetizado; se conoce costo cotizado, no retorno.
Escenario medido: ahorro anual validado A menos O_anual; ROI primer año = (A - O_anual - I) / I × 100, solo si I > 0 y A tiene base real.
Recuperación simple = I / (A - O_anual), solo si A > O_anual.
Para recuperar en N años, ahorro anual requerido A = O_anual + I/N (sin descuento). Es un umbral, no ahorro asegurado.
Si faltan datos de producción y precios no se puede dar ROI exacto ni afirmar rentabilidad.

## CONCLUSIÓN DE VIABILIDAD GLOBAL
La alternativa web en nube es operativa y técnicamente viable bajo capacitación, adquisición y conectividad verificadas. La viabilidad económica queda condicionada a cotizaciones y medición de beneficios; se recomienda un piloto acotado y una decisión de inversión con I, O_anual y metas aprobadas. La disposición financiera del caso no sustituye esa evaluación.
