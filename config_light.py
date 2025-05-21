"""
Configuración para modo de desarrollo ligero (3GB RAM, disco limitado)
"""

class LightConfig:
    # Configuración de recursos
    MAX_RAM_MB = 2048  # Dejamos margen para el SO
    MAX_DISK_GB = 5    # Límite de uso de disco en GB
    
    # Configuración de modelos
    ENABLE_LARGE_MODELS = False
    MODEL_CACHE_SIZE_MB = 500  # Tamaño máximo de caché de modelos
    
    # Configuración de procesamiento
    MAX_WORKERS = 2  # Número máximo de workers paralelos
    BATCH_SIZE = 8   # Tamaño de lote reducido
    
    # Almacenamiento
    USE_SQLITE = True  # Usar SQLite en lugar de PostgreSQL
    ENABLE_VECTOR_STORE = False  # Deshabilitar almacenamiento vectorial
    
    # Módulos habilitados
    MODULES = {
        'nlp': True,         # Procesamiento básico de lenguaje
        'vision': False,     # Deshabilitar visión por computadora
        'audio': False,      # Deshabilitar procesamiento de audio
        'training': False,   # Deshabilitar entrenamiento local
    }
    
    # Configuración de logging
    LOG_LEVEL = 'INFO'
    LOG_FILE = 'frondabrick_light.log'

# Configuración para spaCy
SPACY_CONFIG = {
    'model': 'es_core_news_sm',  # Modelo pequeño en español
    'disable': ['parser', 'ner', 'textcat'],  # Deshabilitar componentes pesados
    'enable': ['tagger', 'morphologizer']  # Solo mantener componentes esenciales
}

# Configuración de la base de datos
DATABASE_CONFIG = {
    'dialect': 'sqlite',
    'database': 'frondabrick_light.db',
    'echo': False
}

# Configuración del servidor
SERVER_CONFIG = {
    'host': '0.0.0.0',
    'port': 8000,
    'reload': True,
    'workers': 1  # Un solo worker para ahorrar memoria
}

# Configuración de caché
CACHE_CONFIG = {
    'backend': 'memory',
    'threshold': 100,  # Máximo 100 elementos en caché
    'default_timeout': 300  # 5 minutos
}
