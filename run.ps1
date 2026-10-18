<#
.SYNOPSIS
    Script de inicio rápido de NewBit (PY-NB-001) para PowerShell en Windows.
.DESCRIPTION
    Inicia el servidor web FastAPI + Uvicorn de NewBit, verificando el entorno virtual
    y ofreciendo la apertura automática en el navegador web predeterminado.
.PARAMETER OpenBrowser
    Abre automáticamente http://127.0.0.1:8000 en el navegador web predeterminado.
#>

[CmdletBinding()]
param (
    [switch]$OpenBrowser
)

$Host.UI.RawUI.WindowTitle = "NewBit (PY-NB-001) - Web Server"
$RootPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $RootPath

Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host "          NEWBIT (PY-NB-001) - SERVIDOR DE DESARROLLO LOCAL" -ForegroundColor Green
Write-Host "   Monitoreo con Visión Artificial en Manufactura Metalmecánica" -ForegroundColor White
Write-Host "   Grupo D3 · Ingeniería de Software II (UNS) · Prof. Dr. Alfredo Daza" -ForegroundColor DarkGray
Write-Host "=======================================================================" -ForegroundColor Cyan
Write-Host ""

# 1. Validar entorno virtual
$VenvPython = Join-Path $RootPath ".venv\Scripts\python.exe"
$VenvUvicorn = Join-Path $RootPath ".venv\Scripts\uvicorn.exe"

if (-not (Test-Path $VenvPython)) {
    Write-Host "[ERROR] No se encontró el entorno virtual en .venv\" -ForegroundColor Red
    Write-Host "Por favor, ejecute los siguientes comandos para crearlo:" -ForegroundColor Yellow
    Write-Host "  python -m venv .venv" -ForegroundColor White
    Write-Host "  .\.venv\Scripts\pip install -r proyecto-newbit\requirements.txt" -ForegroundColor White
    Write-Host ""
    Read-Host "Presione Enter para salir..."
    exit 1
}

# 2. Validar pesos de YOLOv8n
$WeightsPath = Join-Path $RootPath "proyecto-newbit\ml\weights\yolov8n.pt"
if (-not (Test-Path $WeightsPath)) {
    Write-Host "[AVISO] Pesos yolov8n.pt no encontrados en ml/weights/." -ForegroundColor Yellow
    Write-Host "Ultralytics descargará automáticamente el modelo oficial en la primera inferencia." -ForegroundColor DarkGray
    Write-Host ""
} else {
    Write-Host "[OK] Pesos YOLOv8n detectados en: ml/weights/yolov8n.pt" -ForegroundColor Green
}

# 3. Informar endpoints y accesos
Write-Host ""
Write-Host "[INFO] URLs operativas de la plataforma:" -ForegroundColor Cyan
Write-Host "  • Dashboard Principal:    http://127.0.0.1:8000/" -ForegroundColor White
Write-Host "  • Catálogo de Videos:     http://127.0.0.1:8000/videos" -ForegroundColor White
Write-Host "  • Panel de Calibración:   http://127.0.0.1:8000/calibration" -ForegroundColor White
Write-Host "  • Documentación Swagger:  http://127.0.0.1:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "Presione Ctrl+C en cualquier momento para detener el servidor." -ForegroundColor DarkGray
Write-Host "-----------------------------------------------------------------------" -ForegroundColor Cyan

# 4. Apertura opcional del navegador
if ($OpenBrowser) {
    Start-Process "http://127.0.0.1:8000/"
}

# 5. Ejecutar servidor FastAPI con Uvicorn
& $VenvUvicorn app.main:app --app-dir proyecto-newbit --host 127.0.0.1 --port 8000 --reload
