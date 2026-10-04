from pathlib import Path
import argparse
import xml.etree.ElementTree as ET


def geometria(parent, x, y, w, h, relativa=False):
    attrs = {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"}
    if relativa:
        attrs["relative"] = "1"
    return ET.SubElement(parent, "mxGeometry", attrs)


def crear(destino: Path, sobrescribir: bool = False):
    if destino.exists() and not sobrescribir:
        raise FileExistsError(f"Ya existe {destino}; use --force para regenerarlo.")
    mxfile = ET.Element("mxfile", {"host": "app.diagrams.net", "version": "24.7.17"})
    diagram = ET.SubElement(mxfile, "diagram", {"id": "flujo-carriles", "name": "Página-1"})
    model = ET.SubElement(diagram, "mxGraphModel", {"dx": "1200", "dy": "800", "grid": "1", "gridSize": "10", "page": "1", "pageWidth": "1169", "pageHeight": "827"})
    root = ET.SubElement(model, "root")
    ET.SubElement(root, "mxCell", {"id": "0"})
    ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

    swim = ET.SubElement(root, "mxCell", {"id": "2", "value": "Ejemplo técnico: revisión de solicitud", "style": "swimlane;horizontal=0;startSize=30;", "vertex": "1", "parent": "1"})
    geometria(swim, 40, 40, 880, 520)
    carril1 = ET.SubElement(root, "mxCell", {"id": "3", "value": "Solicitante", "style": "swimlane;horizontal=0;startSize=28;", "vertex": "1", "parent": "2"})
    geometria(carril1, 0, 0, 440, 520)
    carril2 = ET.SubElement(root, "mxCell", {"id": "4", "value": "Analista", "style": "swimlane;horizontal=0;startSize=28;", "vertex": "1", "parent": "2"})
    geometria(carril2, 440, 0, 440, 520)

    nodos = [
        ("5", "Inicio", "ellipse;whiteSpace=wrap;html=1;", "3", 80, 60, 90, 50),
        ("6", "Enviar solicitud", "rounded=1;whiteSpace=wrap;html=1;", "3", 65, 160, 150, 60),
        ("7", "Revisar solicitud", "rounded=1;whiteSpace=wrap;html=1;", "4", 110, 160, 150, 60),
        ("8", "¿Está completa?", "rhombus;whiteSpace=wrap;html=1;", "4", 120, 280, 130, 90),
        ("9", "Registrar resultado", "rounded=1;whiteSpace=wrap;html=1;", "4", 105, 420, 160, 60),
        ("10", "Corregir información", "rounded=1;whiteSpace=wrap;html=1;", "3", 60, 330, 170, 60),
    ]
    for ident, valor, estilo, padre, x, y, w, h in nodos:
        celda = ET.SubElement(root, "mxCell", {"id": ident, "value": valor, "style": estilo, "vertex": "1", "parent": padre})
        geometria(celda, x, y, w, h)

    aristas = [
        ("11", "", "5", "6"), ("12", "", "6", "7"), ("13", "", "7", "8"),
        ("14", "Sí", "8", "9"), ("15", "No", "8", "10"), ("16", "Reenviar", "10", "7"),
    ]
    for ident, valor, origen, fin in aristas:
        edge = ET.SubElement(root, "mxCell", {"id": ident, "value": valor, "style": "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;", "edge": "1", "parent": "2", "source": origen, "target": fin})
        geometria(edge, 0, 0, 0, 0, True)

    ET.indent(mxfile, space="  ")
    destino.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(mxfile).write(destino, encoding="utf-8", xml_declaration=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Genera un flujo draw.io editable de ejemplo.")
    parser.add_argument("--salida", type=Path, default=Path("plantillas/flujo/ejemplo-carriles.drawio"))
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()
    crear(args.salida, args.force)
    print(f"Generado: {args.salida}")
