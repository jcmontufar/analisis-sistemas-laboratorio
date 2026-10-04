$ErrorActionPreference = 'Stop'

$comandos = @('git', 'gh', 'java', 'node', 'npm', 'dot', 'python', 'pandoc')
foreach ($nombre in $comandos) {
    $encontrado = Get-Command $nombre -ErrorAction SilentlyContinue
    if ($encontrado) {
        Write-Output ("{0}: DISPONIBLE ({1})" -f $nombre, $encontrado.Source)
    } else {
        Write-Output ("{0}: NO DISPONIBLE" -f $nombre)
    }
}

Write-Output "`nVersiones detectadas:"
if (Get-Command git -ErrorAction SilentlyContinue) { git --version }
if (Get-Command gh -ErrorAction SilentlyContinue) { gh --version | Select-Object -First 1 }
if (Get-Command java -ErrorAction SilentlyContinue) { java -version 2>&1 | Select-Object -First 2 }
if (Get-Command node -ErrorAction SilentlyContinue) { node --version }
if (Get-Command npm -ErrorAction SilentlyContinue) { npm --version }
if (Get-Command dot -ErrorAction SilentlyContinue) { dot -V 2>&1 }
if (Get-Command python -ErrorAction SilentlyContinue) { python --version }
if (Get-Command pandoc -ErrorAction SilentlyContinue) { pandoc --version | Select-Object -First 1 }
