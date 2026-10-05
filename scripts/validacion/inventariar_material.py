from collections import Counter
from pathlib import Path
import hashlib
import sys
import zipfile

from PIL import Image
from pypdf import PdfReader

RAIZ = Path(__file__).resolve().parents[2]
ORIGINALES = RAIZ / "material-didactico" / "originales"
MANIFIESTO = RAIZ / "material-didactico" / "manifiesto-sha256.txt"
FORMATOS_ESPERADOS = {".png": 18, ".pdf": 2, ".pptx": 1, ".md": 1}


def leer_manifiesto():
    esperados = {}
    for linea in MANIFIESTO.read_text(encoding="utf-8").splitlines():
        if not linea.strip():
            continue
        digest, relativo = linea.split(maxsplit=1)
        esperados[relativo.strip()] = digest.upper()
    return esperados


def comprobar_lectura(ruta):
    sufijo = ruta.suffix.lower()
    if sufijo == ".png":
        with Image.open(ruta) as imagen:
            imagen.verify()
    elif sufijo == ".pdf":
        lector = PdfReader(ruta)
        if not lector.pages:
            raise ValueError("PDF sin páginas")
    elif sufijo == ".pptx":
        with zipfile.ZipFile(ruta) as paquete:
            if "[Content_Types].xml" not in paquete.namelist():
                raise ValueError("PPTX sin estructura OOXML")
            paquete.testzip()
    elif sufijo == ".md":
        ruta.read_text(encoding="utf-8")


def main():
    errores = []
    archivos = sorted(p for p in ORIGINALES.iterdir() if p.is_file() and p.name != ".gitkeep")
    esperados = leer_manifiesto()
    formatos = Counter(p.suffix.lower() for p in archivos)
    digests = {}

    if len(archivos) != 22:
        errores.append(f"Se esperaban 22 archivos y se encontraron {len(archivos)}")
    if formatos != Counter(FORMATOS_ESPERADOS):
        errores.append(f"Formatos inesperados: {dict(formatos)}")

    for ruta in archivos:
        relativo = f"originales/{ruta.name}"
        digest = hashlib.sha256(ruta.read_bytes()).hexdigest().upper()
        if relativo not in esperados:
            errores.append(f"No está en manifiesto: {relativo}")
        elif esperados[relativo] != digest:
            errores.append(f"SHA-256 no coincide: {relativo}")
        if digest in digests:
            errores.append(f"Duplicado binario: {relativo} = {digests[digest]}")
        digests[digest] = relativo
        try:
            comprobar_lectura(ruta)
        except Exception as exc:
            errores.append(f"Ilegible/corrupto: {relativo}: {exc}")

    faltantes = sorted(set(esperados) - {f"originales/{p.name}" for p in archivos})
    errores.extend(f"Falta archivo del manifiesto: {x}" for x in faltantes)

    print(f"Materiales: {len(archivos)}; formatos: {dict(sorted(formatos.items()))}")
    print(f"Manifiesto: {len(esperados)} entradas; duplicados: {len(archivos) - len(digests)}")
    print(f"Validación de material: {len(errores)} error(es).")
    for error in errores:
        print(f"ERROR: {error}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
