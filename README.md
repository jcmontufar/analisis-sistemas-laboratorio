# Laboratorio académico de análisis y diseño de sistemas

Infraestructura local para conservar material didáctico, resolver ejercicios, generar diagramas y validar entregables académicos. El proyecto no contiene soluciones de ejercicios reales.

## Requisitos

- Git
- Java 17 o posterior para PlantUML
- Node.js y npm para Mermaid y DBML
- Python 3.10 o posterior para validación y documentos
- Graphviz es recomendable; el instalador local intenta proveer una alternativa sin cambiar Windows.

Las versiones comprobadas y las limitaciones de esta máquina se registran en [`configuracion/herramientas.md`](configuracion/herramientas.md).

## Organización

- `material-didactico/`: originales inmutables, texto extraído e índice trazable.
- `base-conocimiento/`: referencias académicas y notas complementarias por tema.
- `ejercicios/`: una carpeta independiente por ejercicio.
- `plantillas/`: fuentes editables y ejemplos técnicos mínimos.
- `prompts/`: instrucciones reutilizables de generación y revisión.
- `scripts/`: instalación local, generación y validación.
- `configuracion/`: inventario y decisiones de herramientas.
- `pruebas/`: entradas y resultados de las pruebas del entorno.

## Incorporar material didáctico

1. Copiar los originales sin modificarlos a `material-didactico/originales/`.
2. Ejecutar `python scripts/validacion/inventariar_material.py`.
3. Extraer texto únicamente cuando sea confiable y guardarlo en `material-didactico/extraidos/`, indicando archivo y página.
4. Marcar documentos basados en imágenes para revisión visual; no aplicar OCR indiscriminado.
5. Actualizar el tema y el estado de procesamiento en `material-didactico/indice.md`.

## Crear un ejercicio

En PowerShell:

```powershell
./scripts/generacion/nuevo-ejercicio.ps1 -Numero 1
```

Esto crea `ejercicios/ejercicio-001/` con enunciado, análisis, solución, fuentes, exportados, documentos y validación.

## Instalar herramientas locales

```powershell
./scripts/instalacion/instalar-local.ps1
```

El script instala dependencias Node y Python dentro del proyecto y descarga PlantUML en `herramientas-locales/`. No modifica variables de entorno ni configuración global de Windows.

## Generar diagramas

```powershell
./scripts/generacion/generar-plantuml.ps1 plantillas/uml/ejemplo-casos-uso.puml
./scripts/generacion/generar-mermaid.ps1 plantillas/cronograma/ejemplo-gantt.mmd
python scripts/generacion/generar_drawio.py
node scripts/generacion/convertir-dbml.js plantillas/entidad-relacion/ejemplo-modelo.dbml pruebas/salida/modelo.sql postgres
```

PlantUML y Mermaid generan SVG por defecto; use `-Formato png` en los scripts cuando se necesite PNG. El archivo `.drawio` conserva formas, conectores, etiquetas y carriles editables.

## Validar

```powershell
python scripts/validacion/validar_proyecto.py
```

La validación automática comprueba estructura, sintaxis básica, XML de draw.io, archivos editables, vínculos Markdown locales y pares fuente/exportación. La revisión conceptual sigue siendo manual.

## GitHub y recuperación

Antes de publicar, confirme que el repositorio remoto sea privado. Flujo habitual:

```powershell
./scripts/instalacion/gh-local.ps1 auth login
./scripts/instalacion/gh-local.ps1 auth status
git status
git add .
git commit -m "Prepara laboratorio académico"
git push -u origin main
git log --oneline
```

El envoltorio descarga GitHub CLI de forma portátil si no existe y no modifica la instalación global. Tras autenticar, se debe comprobar que no exista un remoto homónimo antes de ejecutar `gh repo create analisis-sistemas-laboratorio --private --source . --remote origin --push`.

Para recuperar una versión anterior sin destruir el trabajo actual, consulte `git log`, cree una rama desde el commit requerido (`git switch -c recuperacion/<nombre> <commit>`) y copie el entregable verificado. Los originales académicos nunca deben publicarse en un repositorio público.
