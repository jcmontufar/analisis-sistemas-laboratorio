param(
    [switch]$OmitirNode,
    [switch]$OmitirPython,
    [switch]$OmitirPlantUML
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
Set-Location $raiz

if (-not $OmitirNode) {
    if (-not (Get-Command npm -ErrorAction SilentlyContinue)) { throw 'npm no está disponible.' }
    npm install
}

if (-not $OmitirPython) {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) { throw 'Python no está disponible.' }
    if (-not (Test-Path '.venv')) { python -m venv .venv }
    & '.\.venv\Scripts\python.exe' -m pip install --upgrade pip
    & '.\.venv\Scripts\python.exe' -m pip install -r requirements.txt
}

if (-not $OmitirPlantUML) {
    if (-not (Get-Command java -ErrorAction SilentlyContinue)) { throw 'Java no está disponible.' }
    $destino = Join-Path $raiz 'herramientas-locales\plantuml\plantuml.jar'
    if (-not (Test-Path $destino)) {
        New-Item -ItemType Directory -Path (Split-Path $destino) -Force | Out-Null
        Invoke-WebRequest -Uri 'https://github.com/plantuml/plantuml/releases/latest/download/plantuml.jar' -OutFile $destino
    }
    java -jar $destino -version
}

Write-Output 'Instalación local terminada. Ejecute scripts/instalacion/comprobar-entorno.ps1 y las pruebas.'
