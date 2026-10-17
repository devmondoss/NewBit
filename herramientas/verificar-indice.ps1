# Script de verificación para Windows PowerShell
# Regla: cada archivo no-Markdown debe estar en una carpeta que contenga <nombre de la carpeta>.md
# Excepciones: infografias (assets web), node_modules, .git, .venv

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path "$PSScriptRoot\..").Path
Set-Location $repoRoot

$faltan = 0

$targetDirs = @("curso", "proyecto-newbit", "descartado") | Where-Object { Test-Path $_ }

foreach ($target in $targetDirs) {
    Get-ChildItem -Path $target -Recurse -File | Where-Object {
        $_.Extension -ne ".md" -and
        $_.Name -ne ".DS_Store" -and
        $_.FullName -notmatch "[\\/]infografias[\\/]" -and
        $_.FullName -notmatch "[\\/]Infografias_NewBit[\\/]" -and
        $_.FullName -notmatch "[\\/]node_modules[\\/]" -and
        $_.FullName -notmatch "[\\/]\.venv[\\/]" -and
        $_.FullName -notmatch "[\\/]\.git[\\/]"
    } | ForEach-Object {
        $parent = $_.Directory
        $expectedMd = Join-Path $parent.FullName ($parent.Name + ".md")
        if (-not (Test-Path $expectedMd)) {
            Write-Host "SIN CARPETA/.md: $($_.FullName)" -ForegroundColor Red
            $faltan++
        }
    }
}

# Archivos no-md sueltos en la raíz (excluyendo archivos ocultos como .gitignore)
Get-ChildItem -Path $repoRoot -File | Where-Object {
    $_.Extension -ne ".md" -and
    -not $_.Name.StartsWith(".")
} | ForEach-Object {
    Write-Host "SIN CLASIFICAR (raíz): $($_.Name)" -ForegroundColor Yellow
    $faltan++
}

if ($faltan -eq 0) {
    Write-Host "OK: cada archivo está en su carpeta con su .md." -ForegroundColor Green
    exit 0
} else {
    Write-Host "Faltan $faltan archivos por clasificar o sin su .md correspondiente." -ForegroundColor Red
    exit 1
}
