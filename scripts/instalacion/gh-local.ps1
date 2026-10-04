param(
    [Parameter(ValueFromRemainingArguments = $true)]
    [string[]]$Argumentos
)

$ErrorActionPreference = 'Stop'
$raiz = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$base = Join-Path $raiz 'herramientas-locales'
$exe = Get-ChildItem $base -Recurse -Filter gh.exe -ErrorAction SilentlyContinue | Select-Object -First 1 -ExpandProperty FullName

if (-not $exe) {
    $release = Invoke-RestMethod -Uri 'https://api.github.com/repos/cli/cli/releases/latest' -Headers @{ 'User-Agent' = 'analisis-sistemas-laboratorio' }
    $asset = $release.assets | Where-Object { $_.name -match '^gh_[0-9.]+_windows_amd64\.zip$' } | Select-Object -First 1
    if (-not $asset) { throw 'No se encontró el paquete oficial de GitHub CLI para Windows amd64.' }
    $version = $release.tag_name.TrimStart('v')
    $zip = Join-Path $base $asset.name
    $destino = Join-Path $base "gh-$version"
    New-Item -ItemType Directory -Path $base -Force | Out-Null
    Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $zip
    Expand-Archive -LiteralPath $zip -DestinationPath $destino -Force
    $exe = Get-ChildItem $destino -Recurse -Filter gh.exe | Select-Object -First 1 -ExpandProperty FullName
}

& $exe @Argumentos
exit $LASTEXITCODE
