param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(1, 999)]
    [int]$Numero
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$nombre = 'ejercicio-{0:D3}' -f $Numero
$destino = Join-Path $raiz "ejercicios\$nombre"
$plantilla = Join-Path $raiz 'plantillas\ejercicio'

if (Test-Path -LiteralPath $destino) { throw "Ya existe $destino; no se sobrescribió." }
if (-not (Test-Path -LiteralPath $plantilla)) { throw "No existe la plantilla maestra: $plantilla" }

@('diagramas\fuentes', 'diagramas\exportados', 'documentos') | ForEach-Object {
    New-Item -ItemType Directory -Path (Join-Path $destino $_) -Force | Out-Null
}

@('enunciado.md', 'analisis.md', 'suposiciones.md', 'fuentes.md', 'solucion.md', 'validacion.md') | ForEach-Object {
    Copy-Item -LiteralPath (Join-Path $plantilla $_) -Destination (Join-Path $destino $_)
}

@('diagramas\fuentes\.gitkeep', 'diagramas\exportados\.gitkeep', 'documentos\.gitkeep') | ForEach-Object {
    New-Item -ItemType File -Path (Join-Path $destino $_) -Force | Out-Null
}

Write-Output "Creado desde plantilla maestra: $destino"
