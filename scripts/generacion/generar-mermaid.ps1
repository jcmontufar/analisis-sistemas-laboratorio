param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Entrada,
    [ValidateSet('svg', 'png', 'pdf')]
    [string]$Formato = 'svg',
    [string]$DirectorioSalida = 'pruebas/salida'
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$rutaEntrada = if ([IO.Path]::IsPathRooted($Entrada)) { $Entrada } else { Join-Path $raiz $Entrada }
$archivo = (Resolve-Path $rutaEntrada).Path
$salida = Join-Path $raiz $DirectorioSalida
$nombre = [IO.Path]::GetFileNameWithoutExtension($archivo) + '.' + $Formato
$destino = Join-Path $salida $nombre

New-Item -ItemType Directory -Path $salida -Force | Out-Null
Push-Location $raiz
try {
    & '.\node_modules\.bin\mmdc.cmd' -i $archivo -o $destino -b transparent
    if ($LASTEXITCODE -ne 0) { throw "Mermaid terminó con código $LASTEXITCODE." }
} finally {
    Pop-Location
}
