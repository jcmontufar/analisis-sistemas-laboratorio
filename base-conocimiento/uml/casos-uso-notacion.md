# Auditoría de notación de casos de uso

Fuentes visuales: `material-didactico/originales/11-CasosDeUsoAccesoAlSistema.png` y `12-CasosDeUsoProceso.png`.

## Convención observada en material académico

### PNG 11: acceso al sistema

- Un actor “Usuario(admin)” se asocia con “ingreso al sistema/login”.
- Desde login salen dependencias discontinuas hacia siete módulos.
- Las puntas de flecha están en los módulos.
- El rótulo visible es `<<extends>>` —plural—.
- La disposición parece comunicar navegación o acceso posterior al login, no un punto de extensión UML formal.

### PNG 12: proceso del coordinador

- `<<include>>`: flecha discontinua desde “Gestionar…” hacia el subcaso incluido. La punta queda en “Asignar técnicos y recursos”, “Generar cotización”, etc.
- `<<extend>>`: flecha discontinua desde “Gestionar mantenimiento de equipo” hacia “Gestionar servicios”. La punta queda en el caso base.
- Esta dirección coincide con la dirección UML estándar si los subcasos `include` son obligatorios y el mantenimiento es una extensión opcional de gestionar servicios.

## Convención UML estándar

- `«include»`: dependencia desde el caso base hacia el caso incluido; se usa para comportamiento obligatorio reutilizado.
- `«extend»`: dependencia desde el caso de extensión hacia el caso base; se usa para comportamiento opcional condicionado.
- Los estereotipos son singulares: `«include»` y `«extend»`.
- La navegación entre módulos o pantallas no se modela por sí sola con estas dependencias.

## Dictamen

| Punto | Resultado |
|---|---|
| PNG 12, dirección de `include` | Compatible con UML estándar |
| PNG 12, dirección de `extend` | Compatible con UML estándar, condicionado a la intención descrita |
| PNG 11, rótulo `extends` | No coincide con el estereotipo estándar singular |
| PNG 11, dirección/semántica | Técnicamente discutible: parece usar `extend` para acceso o navegación |

Durante un ejercicio se prioriza el enunciado del catedrático. Si el enunciado no prescribe una variante, se usa UML estándar y se documenta la diferencia con el ejemplo académico. El original no se modifica.

