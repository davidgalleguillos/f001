#!/bin/bash
# Script para iniciar Frondabrick en modo ligero (Linux/macOS)

echo "[INFO] Iniciando Frondabrick en modo ligero..."
echo "[INFO] Configuración para 3GB RAM y disco limitado"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 no está instalado"
    exit 1
fi

# Verificar si existe el entorno virtual
if [ ! -d "venv" ]; then
    echo "[INFO] Creando entorno virtual..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "[ERROR] No se pudo crear el entorno virtual"
        exit 1
    fi
fi

# Activar entorno virtual
source venv/bin/activate

# Instalar dependencias ligeras
echo "[INFO] Instalando dependencias ligeras..."
pip install -r requirements_light.txt
if [ $? -ne 0 ]; then
    echo "[ERROR] Error al instalar dependencias"
    exit 1
fi

# Crear directorio para datos si no existe
mkdir -p data

# Iniciar el servidor con configuración ligera
echo "[INFO] Iniciando servidor en modo desarrollo ligero..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
