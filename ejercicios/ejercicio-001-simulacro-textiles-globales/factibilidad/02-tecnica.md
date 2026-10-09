# Factibilidad técnica

PDF p. 2: no hay equipos, servidores, móviles, lectores ni cableado. La propuesta debe incorporar la infraestructura necesaria desde cero.

## Alternativas
| Aspecto | Local | Nube administrada |
|---|---|---|
| Disponibilidad | Depende de servidor, energía y redundancia local | Depende de servicio, energía de planta e Internet |
| Mantenimiento | Planta/contratista administra SO, BD, hardware y parches | Proveedor mantiene plataforma; aplicación requiere soporte |
| Escalabilidad | Comprar/ampliar equipo | Ajustar capacidad contratada según demanda |
| Costo operativo | Energía, soporte, respaldo y renovación | Suscripción, Internet y soporte |
| Internet | Operación local puede seguir sin WAN | Necesario para captura central |
| Respaldo | Copia externa y pruebas a cargo de administración | Automatización contratada y copia separada |
| Administración | Mayor carga técnica local | Menor carga de infraestructura, aún requiere gestión |

Recomendación: nube administrada, condicionada a conexión estable y contingencia. Reduce administración local para una planta sin recursos informáticos. Si Internet no cumple pruebas de operación, reconsiderar servidor local; no afirmar captura offline automática.

## Recursos mínimos propuestos
| Recurso | Especificación mínima propuesta | Cantidad lógica | Uso | Justificación |
|---|---|---|---|---|
| Cableado y switch | Cat 6; switch Gigabit con PoE si AP lo requiere | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Equipos fijos y AP | Estabilidad de enlaces |
| Wi-Fi industrial | AP de doble banda, montaje protegido, segmentación y estudio de cobertura | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Dispositivos móviles | Movilidad; validar polvo/interferencia |
| Terminal de uso rudo | Pantalla táctil legible con guantes, protección según ambiente, navegador vigente | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Estación fija | Alternativa a tableta, no compra duplicada |
| Tableta protegida | Pantalla 10 pulgadas, 4 GB RAM, batería para turno o base de carga, carcasa protectora | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Corte/confección/calidad | Interfaz sencilla cerca del proceso |
| Lector | USB/Bluetooth, códigos 1D y texto legible alternativo | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Selección rápida de OT/paquete | Evita tecleo de identificadores |
| Impresora de etiquetas | Transferencia térmica compatible con etiqueta y lector | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Código de empaque | Propuesta necesaria para identificación física |
| Equipo administrativo | 8 GB RAM, SSD, monitor y navegador | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Jefe de Planta | OT y consulta |
| Internet | Enlace empresarial, dimensionado por concurrencia; evaluar enlace de contingencia | Un servicio principal por planta; secundario por evaluación | Acceso nube | Captura centralizada |
| Router/firewall | VLAN, control de acceso, VPN administrativa y doble WAN si procede | Un punto lógico de salida por planta | Seguridad/perímetro | Separar red operativa |
| UPS | Autonomía según carga medida, cierre seguro y protección | POR DEFINIR SEGÚN PUESTOS DE TRABAJO | Router/AP/equipos críticos | Contingencia eléctrica |
| Servicio aplicación | Servicio administrado HTTPS, despliegue y monitoreo | Un servicio lógico inicial | Aplicación Django | Mantenimiento sencillo |
| Base de datos | PostgreSQL administrado, acceso privado, respaldo automático | Una BD lógica | Trazabilidad | Integridad y concurrencia |
| Respaldo/monitoreo | Copia separada cifrada; alertas y prueba de recuperación | Un servicio lógico con retención definida | Continuidad | Objetivo RPO 24 h, RTO 8 h por validar |

Protección del equipo se selecciona tras medir polvo, golpes y líquidos; no atribuir a toda planta una certificación obligatoria. Comprar terminal o tableta por estación según piloto. No se fija número de AP ni ancho de banda sin planos/concurrencia.

## Arquitectura y seguridad
Navegador HTML/CSS/JavaScript mínimo; Django sirve interfaz y API con autenticación por rol; PostgreSQL privado. HTTPS, respaldos separados, logs sin contraseñas y control de acceso. Monolito modular en vez de microservicios. Copias diarias y recuperación probada; disponibilidad/RPO/RTO son objetivos de diseño, no garantías.

Conclusión: técnicamente viable de forma condicionada a adquirir recursos, verificar red/energía, dimensionar carga y contratar soporte. El código de barras apoya trazabilidad; no determina por sí solo una arquitectura.
