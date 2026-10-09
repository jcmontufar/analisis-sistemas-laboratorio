# DFD de contexto y nivel cero

## Objetivo y elementos

El contexto define la frontera mediante un proceso 0, entidades externas y flujos. El nivel cero descompone ese proceso en procesos principales, almacenes y flujos balanceados.

## Reglas académicas explícitas, solo para DERCAS

- Contexto DERCAS: proceso central número 0 con nombre del sistema, entidades de entrada/salida y flujos. Fuente: instrucciones DERCAS, sección “DFD Contexto”; PPTX, diap. 8.
- Nivel cero DERCAS: entidades presentes en los flujos, 2–3 pasos más importantes de cada proceso, todos los flujos nombrados, al menos un almacén conectado por proceso y cada proceso con entrada y salida. Fuente: instrucciones DERCAS, sección “DFD Nivel 0”; PPTX, diap. 8.

## Convenciones complementarias

Balancear flujos externos entre contexto y nivel cero; no conectar entidad–almacén directamente; nombrar procesos con verbo+objeto; evitar procesos sin entrada o salida.

## Ejemplos y alertas

`14-DFDContexto.png` ejemplifica múltiples entidades y flujos y probablemente duplica “Cliente” por diseño. `17-DiagramaDFDNivel0.png` ejemplifica procesos numerados y almacenes. No forman un par: pertenecen a dominios distintos y no permiten comprobar balance. Véase `auditoria-ejemplos.md`. No se declara notación DFD exacta; si el enunciado exige Kendall y Kendall, esa condición gobierna.
