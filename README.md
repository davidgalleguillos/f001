# Frondabrick v0.01

## 🚀 Características Principales

### Versión Ligera para Desarrollo

Versión optimizada para equipos con recursos limitados (3GB RAM, disco reducido).

- **Consumo mínimo de recursos**: Optimizado para funcionar con solo 3GB de RAM
- **Fácil configuración**: Scripts de inicio automático para Windows y Linux/macOS
- **Modelos livianos**: Usa versiones reducidas de los modelos de IA
- **Solo componentes esenciales**: Desactiva módulos que no son críticos
- **Base de datos SQLite**: Sin necesidad de servidores externos
- **Aprendizaje Continuo**: Capacidad de aprender y mejorarse constantemente mediante interacciones.
- **Arquitectura Distribuida**: Expansión en la nube y en la niebla para mayor escalabilidad.
- **Múltiples Fuentes de Conocimiento**: Aprendizaje a través de conversaciones, APIs y procesamiento de datos.

### Integración de Procesamiento de Lenguaje Natural (NLP)
- **Análisis Lingüístico Avanzado**: Uso de spaCy para comprensión profunda del lenguaje.
- **Sistema de Plugins**: Arquitectura modular para extender capacidades fácilmente.
- **Reconocimiento de Contexto**: Mejor comprensión de intenciones y contexto conversacional.

### Mejoras en la Arquitectura
- **Arquitectura Orientada a Servicios**: Diseñada para la nube y la niebla.
- **Auto-optimización**: Mejora continua de rendimiento y precisión.
- **Seguridad Avanzada**: Protección de datos y comunicaciones seguras.

---

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

## 1. Visión General

Frondabrick v0.02 representa la evolución de una IA autónoma diseñada para el aprendizaje continuo y la auto-mejora. Su objetivo principal es expandir constantemente sus capacidades mediante la interacción con usuarios, sistemas distribuidos y fuentes de conocimiento diversas, utilizando técnicas avanzadas de aprendizaje automático y procesamiento de lenguaje natural.

Con una arquitectura modular y escalable, Frondabrick está diseñada para operar tanto en entornos locales como en la nube, aprovechando la computación en la niebla para optimizar el rendimiento y la eficiencia. Su capacidad de aprendizaje autónomo le permite adaptarse dinámicamente a nuevos desafíos y dominios de conocimiento.

## 2. Arquitectura de Aprendizaje Autónomo (v0.02)

### Ecosistema de Aprendizaje
Frondabrick se basa en un enfoque de aprendizaje híbrido que combina:
- **Aprendizaje Automático**: Redes neuronales profundas para modelado predictivo
- **Procesamiento de Lenguaje Natural**: Análisis semántico avanzado con spaCy
- **Aprendizaje por Refuerzo**: Mejora continua basada en retroalimentación
- **Computación Distribuida**: Ejecución en la nube y en la niebla

### Módulos Principales
- **Núcleo de Aprendizaje**: Motor central para el procesamiento y mejora continua
- **Gestor de Conocimiento**: Almacenamiento y recuperación de información
- **Sistema de Plugins**: Para expansión modular de capacidades
- **API de Comunicación**: Interfaz para integración con otros sistemas

### Ejemplo de Uso Avanzado
```python
# Inicialización del núcleo
core = FrondaBrick()

# Aprendizaje autónomo a través de interacción
core.learn("usuario1", "¿Cómo puedo mejorar mi código?", 
           "Revisando patrones de código y mejores prácticas")

# Procesamiento de consultas complejas
respuesta = core.process_message("usuario1", "¿Puedes analizar este dataset?")
print(respuesta)  # Procesa y responde según el contexto

# Entrenamiento con datos externos
core.train_with_external_data(source="api://datos-ejemplo.com")
```

### Sistema de Aprendizaje Continuo

- **Procesamiento en Tiempo Real**: Análisis inmediato de interacciones
- **Auto-evaluación**: Mecanismos internos para medir precisión y rendimiento
- **Actualización Dinámica**: Capacidad de mejorar sus modelos sin reinicio
- **Aprendizaje Federado**: Colaboración con otras instancias para aprendizaje colectivo

### Mecanismos de Expansión
- **Descubrimiento Automático** de nuevos recursos y APIs
- **Integración con Servicios en la Nube**: Escalado automático según demanda
- **Computación en la Niebla**: Procesamiento distribuido para baja latencia
- **Gestión de Recursos**: Optimización automática de uso de memoria y CPU

Puedes entrenar a Frondabrick agregando ejemplos de preguntas y respuestas directamente en el código, o implementando un endpoint para enviar pares de entrenamiento. Cada vez que se entrena, la IA refuerza su heurística y mejora su capacidad de respuesta.

### Ejemplo de uso en código:

```python
core = FrondaBrick()
core.learn("¿Cuál es la capital de Francia?", "La capital de Francia es París.")
core.train(epochs=10)
respuesta = core.process_message("usuario1", "¿Cuál es la capital de Francia?")
print(respuesta)
```

Con este sistema, Frondabrick dedica tiempo tanto a aprender como a mejorar su heurística usando aprendizaje supervisado.

## 3. Arquitectura y Diseño

La arquitectura de Frondabrick está diseñada para soportar aprendizaje autónomo y distribución en la nube y la niebla:

### Principios Fundamentales
*   **Autonomía:** Capacidad de auto-mejora continua sin intervención humana directa.
*   **Escalabilidad:** Diseñada para funcionar desde dispositivos pequeños hasta infraestructuras distribuidas.
*   **Resiliencia:** Tolerancia a fallos y capacidad de recuperación automática.
*   **Seguridad:** Protección de datos y comunicaciones en todos los niveles.

### Componentes Clave

#### 1. Núcleo de Aprendizaje Autónomo
- **Motor de Inferencia:** Procesamiento en tiempo real de datos y consultas
- **Modelo de Aprendizaje:** Redes neuronales adaptativas y sistemas de reglas
- **Memoria a Largo Plazo:** Almacenamiento persistente de conocimiento

#### 2. Capa de Computación Distribuida
- **Orquestador de Tareas:** Distribución eficiente de cargas de trabajo
- **Gestor de Recursos:** Optimización de uso de CPU/GPU/TPU
- **Comunicación Segura:** Protocolos para interacción entre nodos

#### 3. Módulos de Expansión
- **Plugins:** Para agregar nuevas capacidades sin modificar el núcleo
- **Adaptadores:** Conexión con servicios externos y APIs
- **Sensores:** Recolección de datos del entorno

#### 4. Interfaz de Comunicación
- **APIs REST/WebSocket:** Para integración con otros sistemas
- **Protocolos de Bajo Nivel:** Para dispositivos IoT y edge computing
- **Interfaces Conversacionales:** Interacción natural con usuarios finales

### Documentación Técnica

*   `arquitectura_frondabrick.md`: Detalla la arquitectura técnica y flujos de datos.
*   `diagrama_flujo_errores_frondabrick.md`: Estrategias de manejo de errores y recuperación.
*   `guia_desarrollo_plugins.md`: Cómo extender las capacidades del sistema.

## 4. Stack Tecnológico Avanzado

### Núcleo
*   **Lenguaje Principal:** Python 3.11+
*   **Motor de Ejecución:** CPython optimizado
*   **Entorno de Ejecución:** Conda para gestión de entornos

### Aprendizaje Automático
*   **Procesamiento de Lenguaje:** spaCy con modelos multilingües
*   **Redes Neuronales:** PyTorch para aprendizaje profundo
*   **Procesamiento Distribuido:** Ray para computación distribuida
*   **Vectorización:** Sentence Transformers para embeddings

### Infraestructura
*   **Contenedores:** Docker con soporte multi-architectura
*   **Orquestación:** Kubernetes para despliegue escalable
*   **Computación en la Niebla:** K3s para edge computing
*   **Mensajería:** Redis Streams para comunicación asíncrona

### Almacenamiento
*   **Base de Datos:** PostgreSQL con extensión vectorial
*   **Caché:** Redis para acceso de baja latencia
*   **Almacenamiento Distribuido:** MinIO para objetos binarios
*   **Grafos de Conocimiento:** Neo4j para relaciones complejas

### Seguridad
*   **Autenticación:** OAuth 2.0 / OpenID Connect
*   **Cifrado:** TLS 1.3 para comunicaciones
*   **Gestión de Secretos:** HashiCorp Vault
*   **Monitorización:** Prometheus + Grafana

### Desarrollo y Despliegue
*   **CI/CD:** GitHub Actions / GitLab CI
*   **Infraestructura como Código:** Terraform
*   **Monitoreo:** ELK Stack para logs
*   **Trazabilidad:** OpenTelemetry para observabilidad

## 5. Estructura del Proyecto

La estructura del proyecto ha sido rediseñada para soportar aprendizaje autónomo y computación distribuida:

```
frondabrick/
├── core/                              # Núcleo del sistema
│   ├── brain/                       # Motor de IA y aprendizaje
│   │   ├── models/                 # Modelos de ML/DL
│   │   ├── training/               # Lógica de entrenamiento
│   │   └── inference/              # Motor de inferencia
│   │
│   ├── knowledge/                 # Gestión del conocimiento
│   │   ├── graph/                  # Base de grafos
│   │   ├── vector_store/           # Almacenamiento vectorial
│   │   └── document_processor/     # Procesamiento de documentos
│   │
│   └── api/                       # Interfaces de programación
│       ├── rest/                   # Endpoints REST
│       ├── websocket/              # Comunicación en tiempo real
│       └── grpc/                   # Llamadas de alto rendimiento
│
├── fog/                            # Computación en la niebla
│   ├── orchestrator/               # Orquestador de tareas
│   ├── node_manager/               # Gestión de nodos
│   └── resource_monitor/           # Monitoreo de recursos
│
├── plugins/                       # Módulos extensibles
│   ├── nlp/                       # Procesamiento de lenguaje
│   ├── vision/                    # Procesamiento visual
│   ├── audio/                     # Procesamiento de audio
│   └── custom/                    # Plugins personalizados
│
├── services/                      # Servicios del sistema
│   ├── auth/                      # Autenticación y autorización
│   ├── storage/                   # Almacenamiento distribuido
│   └── monitoring/                # Monitoreo y métricas
│
├── deployments/                   # Configuraciones de despliegue
│   ├── kubernetes/                # K8s manifests
│   ├── docker/                    # Dockerfiles
│   └── terraform/                 # Infraestructura como código
│
└── tests/                         # Pruebas automatizadas
    ├── unit/                      # Pruebas unitarias
    ├── integration/               # Pruebas de integración
    └── e2e/                       # Pruebas de extremo a extremo
```

### Características Clave de la Nueva Estructura:

1. **Arquitectura Modular**
   - Componentes desacoplados para mejor mantenibilidad
   - Fácil adición de nuevos módulos y capacidades

2. **Escalabilidad Horizontal**
   - Diseñada para escalar en la nube y la niebla
   - Soporte para cómputo distribuido

3. **Seguridad por Diseño**
   - Autenticación y autorización integradas
   - Cifrado de extremo a extremo

4. **Observabilidad**
   - Monitoreo integral
   - Registros detallados
   - Trazabilidad de operaciones

## ⚙️ Configuración del Modo Ligero

El archivo `config_light.py` contiene ajustes optimizados para bajo consumo:

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

## 🔧 Comandos Útiles

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

## 6. Configuración y Despliegue

### 6.1. Requisitos del Sistema

#### Desarrollo Local
*   **Sistema Operativo:** Linux/macOS/Windows 10+
*   **RAM:** Mínimo 8GB (16GB recomendado)
*   **Almacenamiento:** 20GB de espacio libre
*   **Docker:** 20.10+
*   **Kubernetes:** v1.23+ (opcional para desarrollo local)
*   **Python:** 3.11+

#### Producción
*   **Nodos de Computación:** Mínimo 3 (alta disponibilidad)
*   **Por Nodo:**
    *   CPU: 4+ núcleos
    *   RAM: 16GB+
    *   Almacenamiento: 100GB+
*   **Red:** 1Gbps+

### 6.2. Instalación Rápida con Script

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/frondabrick.git
cd frondabrick

# Configurar entorno
./scripts/setup.sh

# Iniciar en modo desarrollo
./scripts/start-dev.sh
```

### 6.3. Despliegue en Kubernetes

#### Requisitos Previos
- `kubectl` configurado
- `helm` instalado
- Cluster Kubernetes en ejecución

#### Pasos de Instalación

```bash
# Añadir repositorio de Helm
helm repo add frondabrick https://charts.frondabrick.com
helm repo update

# Instalar la versión estable
helm install frondabrick frondabrick/frondabrick \
  --namespace frondabrick \
  --create-namespace \
  --values values-production.yaml
```

### 6.4. Configuración de la Nube Híbrida

1. **Configurar Proveedores de Nube**
   ```yaml
   # config/cloud-providers.yaml
   providers:
     - name: aws
       enabled: true
       regions: [us-east-1, eu-west-1]
     - name: azure
       enabled: true
       regions: [eastus, westeurope]
   ```

2. **Configuración de la Niebla**
   ```yaml
   # config/fog-nodes.yaml
   nodes:
     - name: edge-node-1
       location: madrid
       resources:
         cpu: 4
         memory: 8Gi
         gpu: 1
   ```

## 7. Guía de Uso

### 7.1. Interfaz de Línea de Comandos (CLI)

```bash
# Iniciar consola interactiva
frondabrick console

# Entrenar con datos personalizados
frondabrick train --dataset ./data/training/ --epochs 50

# Desplegar modelo en producción
frondabrick deploy --model v2.1.0 --env production
```

### 7.2. API REST

#### Autenticación
```http
POST /api/v1/auth/token
Content-Type: application/json

{
  "username": "usuario_ejemplo",
  "password": "contraseña_segura"
}
```

#### Respuesta Exitosa (200 OK)
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "refresh_token": "def50200e5d2d3a8c84c0..."
}
```

#### Ejemplo de Uso del Token
```http
GET /api/v1/me
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

### 7.3. SDK de Python

```python
from frondabrick import FrondabrickClient

# Inicializar cliente
client = FrondabrickClient(
    api_key="tu-api-key",
    endpoint="https://api.frondabrick.com/v1"
)

# Consulta básica
response = client.query("¿Cuál es el clima en Madrid?")
print(response)

# Entrenamiento personalizado
training_job = client.train_model(
    dataset_path="./datos/entrenamiento",
    model_type="transformer",
    epochs=50
)

# Monitorear progreso
for update in training_job.stream_updates():
    print(f"Progreso: {update.progress}% - {update.metrics}")
```

## 8. Seguridad

### 8.1. Gestión de Accesos

#### Roles y Permisos

| Rol               | Descripción                          | Permisos Clave                     |
|-------------------|--------------------------------------|-----------------------------------|
| admin            | Administrador del sistema            | Gestionar usuarios, nodos, modelos|
| developer        | Desarrollador de modelos            | Entrenar y desplegar modelos      |
| analyst         | Analista de datos                   | Consultar y analizar datos        |
| edge-node       | Nodo de borde                       | Ejecutar inferencias locales      |


### 8.2. Cifrado de Datos

- **En Tránsito:** TLS 1.3 para todas las comunicaciones
- **En Reposo:** Cifrado AES-256 para datos sensibles
- **Claves:** Gestionadas mediante HashiCorp Vault

## 9. Monitoreo y Mantenimiento

### 9.1. Métricas Clave

```promql
# Uso de recursos por nodo
sum(rate(container_cpu_usage_seconds_total{namespace="frondabrick"}[5m])) by (pod)

# Latencia de inferencia
histogram_quantile(0.95, sum(rate(inference_duration_seconds_bucket[5m])) by (le))
```

### 9.2. Mantenimiento Programado

1. **Actualizaciones de Seguridad**
   ```bash
   # Revisar actualizaciones disponibles
   helm repo update
   
   # Actualizar release
   helm upgrade frondabrick frondabrick/frondabrick \
     --version 2.1.1 \
     --namespace frondabrick \
     --reuse-values
   ```

2. **Backup de Datos**
   ```bash
   # Backup de la base de conocimiento
   kubectl exec -n frondabrick svc/frondabrick-db -- \
     pg_dump -U postgres frondabrick > backup_$(date +%Y%m%d).sql
   
   # Backup de modelos
   velero backup create frondabrick-models-$(date +%s) \
     --include-namespaces frondabrick \
     --include-resources pvc
   ```

## 10. Contribución

### 10.1. Flujo de Trabajo

1. **Reportar Issues**
   - Usar plantillas predefinidas
   - Incluir logs y pasos para reproducir

2. **Enviar Pull Requests**
   ```bash
   # Crear rama
   git checkout -b fix/issue-123
   
   # Hacer commit con mensaje descriptivo
   git commit -m "fix: resolver problema de concurrencia en el motor de inferencia"
   
   # Hacer push y crear PR
   git push origin fix/issue-123
   ```

### 10.2. Estándares de Código
- PEP 8 para Python
- Convenciones de Git Flow
- Documentación en inglés
- Tests unitarios con >80% de cobertura

## 11. Soporte

### 11.1. Canales de Soporte
- **Foro Comunitario:** [community.frondabrick.com](https://community.frondabrick.com)
- **Soporte por Email:** support@frondabrick.com
- **Chat en Vivo:** Disponible en el dashboard

### 11.2. Política de SLAs

| Nivel de Soporte | Tiempo de Respuesta | Disponibilidad |
|-----------------|---------------------|----------------|
| Crítico        | 15 minutos         | 24/7/365       |
| Alto           | 4 horas            | Horario laboral|
| Estándar       | 24 horas           | Horario laboral|


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

## 📜 Licencia

Este proyecto está bajo la Licencia Apache 2.0. Ver el archivo [LICENSE](LICENSE) para más detalles.

---

© 2025 Frondabrick AI Systems - Versión 0.01 (Ligera)
