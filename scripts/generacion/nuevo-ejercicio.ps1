param(
    [Parameter(Mandatory = $true)]
    [ValidateRange(1, 999)]
    [int]$Numero
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$nombre = 'ejercicio-{0:D3}' -f $Numero
$destino = Join-Path $raiz "ejercicios\$nombre"
if (Test-Path $destino) { throw "Ya existe $destino; no se sobrescribió." }

@('diagramas\fuentes', 'diagramas\exportados', 'documentos') | ForEach-Object {
    New-Item -ItemType Directory -Path (Join-Path $destino $_) -Force | Out-Null
}

$archivos = @{
    'enunciado.md' = "# Enunciado original`n`n[Copiar sin reinterpretar. Indicar origen.]`n"
    'analisis.md' = "# Análisis`n`n## Hechos`n`n## Actores y entidades`n`n## Procesos y relaciones`n`n## Datos faltantes`n`n## Suposiciones`n"
    'solucion.md' = "# Solución`n`n[Desarrollo y explicación académica.]`n"
    'validacion.md' = "# Validación`n`n- [ ] Corresponde al enunciado.`n- [ ] Notación correcta.`n- [ ] DFD balanceados, si aplica.`n- [ ] Actores y relaciones revisados.`n- [ ] Multiplicidades revisadas.`n- [ ] Secuencias coherentes.`n- [ ] Fuente editable disponible.`n- [ ] Exportación completa y legible.`n"
    'diagramas\fuentes\.gitkeep' = ''
    'diagramas\exportados\.gitkeep' = ''
    'documentos\.gitkeep' = ''
}

foreach ($relativo in $archivos.Keys) {
    $ruta = Join-Path $destino $relativo
    Set-Content -LiteralPath $ruta -Value $archivos[$relativo] -Encoding utf8NoBOM
}
Write-Output "Creado: $destino"
