@echo off
REM =========================================================================
REM NewBit (PY-NB-001) - Script de Inicio Rápido para Windows (Batch / CMD)
REM Sistema web con Visión Artificial para la detección de actos inseguros
REM Grupo D3 - Ingeniería de Software II (UNS)
REM =========================================================================

title NewBit Platform (PY-NB-001) - Web Server
cd /d "%~dp0"

echo =======================================================================
echo          NEWBIT (PY-NB-001) - SERVIDOR DE DESARROLLO LOCAL
echo   Monitoreo con Vision Artificial en Manufactura Metalmecanica
echo =======================================================================
echo.

REM 1. Verificar existencia del entorno virtual
if not exist ".venv\Scripts\python.exe" (
    echo [ERROR] No se encontro el entorno virtual en .venv\
    echo Por favor, cree el entorno ejecutando:
    echo   python -m venv .venv
    echo   .\.venv\Scripts\pip install -r proyecto-newbit\requirements.txt
    echo.
    pause
    exit /b 1
)

REM 2. Verificar pesos de YOLOv8n
if not exist "proyecto-newbit\ml\weights\yolov8n.pt" (
    echo [AVISO] Pesos yolov8n.pt no encontrados en ml\weights\.
    echo Ultralytics descargara automaticamente los pesos oficiales en el primer arranque.
    echo.
)

REM 3. Informar URLs operativas
echo [INFO] Iniciando servidor web FastAPI + Uvicorn...
echo [INFO] Dashboard Principal:    http://127.0.0.1:8000/
echo [INFO] Catalogo de Videos:     http://127.0.0.1:8000/videos
echo [INFO] Panel de Calibracion:   http://127.0.0.1:8000/calibration
echo [INFO] Documentacion Swagger:  http://127.0.0.1:8000/docs
echo.
echo Presione Ctrl+C en cualquier momento para detener el servidor.
echo -----------------------------------------------------------------------

REM 4. Lanzar servidor
".venv\Scripts\uvicorn.exe" app.main:app --app-dir proyecto-newbit --host 127.0.0.1 --port 8000 --reload

pause
