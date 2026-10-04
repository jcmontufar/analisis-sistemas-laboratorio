param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Entrada,
    [ValidateSet('svg', 'png')]
    [string]$Formato = 'svg',
    [string]$DirectorioSalida = 'pruebas/salida'
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$jar = Join-Path $raiz 'herramientas-locales\plantuml\plantuml.jar'
$rutaEntrada = if ([IO.Path]::IsPathRooted($Entrada)) { $Entrada } else { Join-Path $raiz $Entrada }
$archivo = (Resolve-Path $rutaEntrada).Path
$salida = Join-Path $raiz $DirectorioSalida

if (-not (Test-Path $jar)) { throw 'Falta PlantUML. Ejecute scripts/instalacion/instalar-local.ps1.' }
New-Item -ItemType Directory -Path $salida -Force | Out-Null
java -jar $jar "-t$Formato" -charset UTF-8 -o $salida $archivo
if ($LASTEXITCODE -ne 0) { throw "PlantUML terminó con código $LASTEXITCODE." }
