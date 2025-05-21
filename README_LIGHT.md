# Frondabrick - Modo Ligero

Versión optimizada para desarrollo en equipos con recursos limitados (3GB RAM, disco limitado).

## 🚀 Características del Modo Ligero

- **Consumo mínimo de RAM**: Optimizado para funcionar con solo 3GB de RAM
- **Espacio en disco reducido**: Requiere menos de 5GB de espacio
- **Modelos livianos**: Usa versiones reducidas de los modelos de IA
- **Solo componentes esenciales**: Desactiva módulos que no son críticos
- **Base de datos SQLite**: Sin necesidad de servidores de base de datos externos

## 🛠️ Requisitos Mínimos

- **Sistema Operativo**: Windows 10/11, macOS 10.15+, o Linux
- **RAM**: Mínimo 3GB (4GB recomendado)
- **Disco Duro**: 5GB de espacio libre
- **Python**: 3.9 o superior

## 🚀 Inicio Rápido

### Windows

1. Descarga o clona el repositorio
2. Haz doble clic en `scripts/start_light.bat`

### Linux/macOS

```bash
# Dar permisos de ejecución
chmod +x scripts/start_light.sh

# Iniciar
./scripts/start_light.sh
```

## 📦 Módulos Incluidos

- **NLP Básico**: Procesamiento de texto con spaCy (modelo pequeño)
- **API REST**: Endpoints básicos para interacción
- **Base de Datos**: SQLite para almacenamiento local
- **Autenticación**: JWT para seguridad básica

## ⚙️ Configuración

El archivo `config_light.py` contiene ajustes optimizados para bajo consumo. Puedes modificar:

```python
class LightConfig:
    MAX_RAM_MB = 2048       # Límite de RAM en MB
    MAX_DISK_GB = 5         # Límite de disco en GB
    ENABLE_LARGE_MODELS = False  # Desactiva modelos grandes
    
    # Habilitar/deshabilitar módulos
    MODULES = {
        'nlp': True,       # Procesamiento de lenguaje
        'vision': False,    # Visión por computadora
        'audio': False,     # Procesamiento de audio
        'training': False   # Entrenamiento local
    }
```

## 🛠️ Comandos Útiles

### Crear entorno virtual manualmente

```bash
# Windows
python -m venv venv
call venv\Scripts\activate

# Linux/macOS
python3 -m venv venv
source venv/bin/activate
```

### Instalar dependencias manualmente

```bash
pip install -r requirements_light.txt
```

### Iniciar servidor manualmente

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

## 🔍 Solución de Problemas

### Error de memoria insuficiente
- Reduce `MAX_RAM_MB` en `config_light.py`
- Cierra otras aplicaciones que consuman mucha memoria

### Error de espacio en disco
- Limpia archivos temporales
- Elimina modelos no utilizados en `fronda_brick_core/data`

## 📚 Recursos Adicionales

- [Documentación de FastAPI](https://fastapi.tiangolo.com/)
- [Documentación de spaCy](https://spacy.io/)
- [Guía de SQLite](https://www.sqlite.org/docs.html)

---

© 2025 Frondabrick AI Systems - Versión Ligera
