from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

RAIZ = Path(__file__).resolve().parents[2]
ERRORES = []
AVISOS = []
EXCLUIDOS = {".git", ".venv", "node_modules", "herramientas-locales", ".cache"}

REQUERIDOS = [
    "AGENTS.md", "README.md", ".gitignore", "material-didactico/originales",
    "material-didactico/extraidos", "material-didactico/indice.md", "base-conocimiento/fundamentos",
    "base-conocimiento/requerimientos", "base-conocimiento/factibilidad", "base-conocimiento/procesos",
    "base-conocimiento/dfd", "base-conocimiento/uml", "base-conocimiento/bases-datos",
    "base-conocimiento/arquitectura", "base-conocimiento/criterios-evaluacion", "ejercicios",
    "plantillas/factibilidad", "plantillas/cronograma", "plantillas/procesos", "plantillas/flujo",
    "plantillas/arquitectura", "plantillas/dfd", "plantillas/entidad-relacion",
    "plantillas/diccionario-datos", "plantillas/prototipo", "plantillas/uml",
    "prompts/generacion", "prompts/revision", "scripts/instalacion", "scripts/generacion",
    "scripts/validacion", "configuracion/herramientas.md",
]


def archivos(patron):
    for ruta in RAIZ.rglob(patron):
        if EXCLUIDOS.isdisjoint(ruta.relative_to(RAIZ).parts):
            yield ruta


def validar_estructura():
    for relativo in REQUERIDOS:
        if not (RAIZ / relativo).exists():
            ERRORES.append(f"Falta: {relativo}")


def validar_plantuml():
    for ruta in archivos("*.puml"):
        texto = ruta.read_text(encoding="utf-8")
        if "@startuml" not in texto or "@enduml" not in texto:
            ERRORES.append(f"PlantUML sin delimitadores: {ruta.relative_to(RAIZ)}")


def validar_mermaid():
    inicios = ("flowchart", "graph", "sequenceDiagram", "classDiagram", "stateDiagram", "erDiagram", "gantt", "journey", "pie", "mindmap", "timeline")
    for ruta in archivos("*.mmd"):
        primera = next((x.strip() for x in ruta.read_text(encoding="utf-8").splitlines() if x.strip()), "")
        if not primera.startswith(inicios):
            ERRORES.append(f"Mermaid sin declaración reconocida: {ruta.relative_to(RAIZ)}")


def validar_drawio():
    for ruta in archivos("*.drawio"):
        try:
            root = ET.parse(ruta).getroot()
            if root.tag != "mxfile" or root.find(".//mxGraphModel") is None:
                ERRORES.append(f"draw.io sin estructura editable: {ruta.relative_to(RAIZ)}")
            if root.find(".//mxCell[@edge='1']") is None:
                AVISOS.append(f"draw.io sin conectores: {ruta.relative_to(RAIZ)}")
        except ET.ParseError as exc:
            ERRORES.append(f"XML inválido en {ruta.relative_to(RAIZ)}: {exc}")


def validar_dbml():
    for ruta in archivos("*.dbml"):
        texto = ruta.read_text(encoding="utf-8")
        if not re.search(r"(?m)^Table\s+\w+\s*\{", texto):
            ERRORES.append(f"DBML sin tabla: {ruta.relative_to(RAIZ)}")


def validar_enlaces_markdown():
    patron = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for ruta in archivos("*.md"):
        texto = ruta.read_text(encoding="utf-8")
        for destino in patron.findall(texto):
            destino = destino.strip().split("#", 1)[0]
            if not destino or "://" in destino or destino.startswith("mailto:"):
                continue
            if not (ruta.parent / destino).resolve().exists():
                ERRORES.append(f"Enlace local roto en {ruta.relative_to(RAIZ)}: {destino}")


def validar_ejercicios():
    for carpeta in (RAIZ / "ejercicios").glob("ejercicio-[0-9][0-9][0-9]"):
        for requerido in ("enunciado.md", "analisis.md", "solucion.md", "validacion.md", "diagramas/fuentes", "diagramas/exportados", "documentos"):
            if not (carpeta / requerido).exists():
                ERRORES.append(f"Ejercicio incompleto {carpeta.name}: falta {requerido}")


def main():
    validar_estructura()
    validar_plantuml()
    validar_mermaid()
    validar_drawio()
    validar_dbml()
    validar_enlaces_markdown()
    validar_ejercicios()
    print(f"Validación automática: {len(ERRORES)} error(es), {len(AVISOS)} aviso(s).")
    for item in ERRORES:
        print(f"ERROR: {item}")
    for item in AVISOS:
        print(f"AVISO: {item}")
    print("Pendiente siempre: revisión conceptual y correspondencia exacta con el enunciado.")
    return 1 if ERRORES else 0


if __name__ == "__main__":
    sys.exit(main())
