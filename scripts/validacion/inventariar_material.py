from pathlib import Path
import hashlib

RAIZ = Path(__file__).resolve().parents[2]
ORIGINALES = RAIZ / "material-didactico" / "originales"


def main():
    archivos = sorted(p for p in ORIGINALES.rglob("*") if p.is_file() and p.name != ".gitkeep")
    print(f"Materiales encontrados: {len(archivos)}")
    for ruta in archivos:
        digest = hashlib.sha256(ruta.read_bytes()).hexdigest()
        relativo = ruta.relative_to(RAIZ).as_posix()
        print(f"{relativo}\t{ruta.suffix.lower() or 'sin extensión'}\t{ruta.stat().st_size} bytes\tsha256:{digest}")
    if not archivos:
        print("No hay originales disponibles; no se realizó extracción.")


if __name__ == "__main__":
    main()
