@echo off
REM Script para iniciar Frondabrick en modo ligero

echo [INFO] Iniciando Frondabrick en modo ligero...
echo [INFO] Configuración para 3GB RAM y disco limitado

REM Verificar Python
python --version >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python no está instalado o no está en el PATH
    pause
    exit /b 1
)

REM Verificar si existe el entorno virtual
if not exist "venv\Scripts\activate" (
    echo [INFO] Creando entorno virtual...
    python -m venv venv
    if %ERRORLEVEL% neq 0 (
        echo [ERROR] No se pudo crear el entorno virtual
        pause
        exit /b 1
    )
)

REM Activar entorno virtual
call venv\Scripts\activate

REM Instalar dependencias ligeras
echo [INFO] Instalando dependencias ligeras...
pip install -r requirements_light.txt
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Error al instalar dependencias
    pause
    exit /b 1
)

REM Crear directorio para datos si no existe
if not exist "data" mkdir data

REM Iniciar el servidor con configuración ligera
echo [INFO] Iniciando servidor en modo desarrollo ligero...
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

pause
