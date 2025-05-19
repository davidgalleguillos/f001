# Dockerfile para Frondabrick v0.01
FROM python:3.10-slim

# Variables de entorno
ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

# Copiar requirements y código
COPY requirements.txt ./
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install numpy
COPY . .

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando de ejecución por defecto
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
