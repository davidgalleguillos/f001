# Frondabrick v0.01

## 1. Descripción General

Frondabrick v0.01 es una Inteligencia Artificial (IA) avanzada y modular, diseñada con capacidad de aprendizaje autónomo. Su objetivo principal es interactuar con los usuarios a través de una interfaz conversacional en tiempo real mediante WebSockets. La IA está construida para aprender de estas interacciones, gestionar su conocimiento y reglas a través de una base de datos SQLite, y tiene la capacidad de realizar tareas avanzadas.

Este proyecto prioriza el desarrollo y las pruebas con componentes reales, evitando simulaciones o mocks, y está diseñado con una arquitectura orientada a la futura integración con un entorno de computación distribuida localmente ("Niebla").

## 2. Sistema de Aprendizaje Autónomo (v0.01)

A partir de la versión 0.01, Frondabrick integra un sistema de aprendizaje real basado en una red neuronal multicapa simple, implementada desde cero en Python:

- Cada mensaje recibido se convierte en un vector y es procesado por la red neuronal, que genera una respuesta vectorizada.
- Las interacciones se almacenan y pueden usarse para entrenar la red, permitiendo que la IA aprenda y mejore sus respuestas con el tiempo.
- El método `learn` permite enseñar a Frondabrick nuevas asociaciones entrada/salida, y el método `train` entrena la red con toda la memoria acumulada.
- Si la IA no reconoce un patrón, responde que aún está aprendiendo y solicita ejemplos.

### Entrenamiento y Mejora

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

## 2. Arquitectura y Diseño

La arquitectura de Frondabrick se basa en los siguientes principios:

*   **Modularidad:** Componentes con responsabilidades claras para facilitar el mantenimiento y la escalabilidad.
*   **Rendimiento Optimizado:** Uso de Python 3.11+, FastAPI y WebSockets.
*   **Persistencia Robusta:** Base de datos SQLite para el conocimiento, reglas e historial.
*   **Orientación a la Niebla:** Diseño que facilita la futura distribución de tareas.

Los documentos detallados sobre la arquitectura y el flujo del sistema son:

*   `arquitectura_frondabrick.md`: Describe los componentes principales, sus interacciones y la estructura de directorios.
*   `diagrama_flujo_errores_frondabrick.md`: Detalla los flujos de interacción conversacional, el proceso de aprendizaje y la estrategia de manejo de errores.

## 3. Stack Tecnológico Principal

*   **Lenguaje de Programación:** Python 3.11+
*   **Framework Web y API:** FastAPI
*   **Servidor ASGI:** Uvicorn
*   **Comunicación en Tiempo Real:** WebSockets
*   **Base de Datos:** SQLite 3
*   **Contenerización:** Docker (Dockerfile proporcionado)
*   **Dependencias Principales:** Ver `requirements.txt` (incluye `fastapi`, `uvicorn`, `websockets`, etc.)

## 4. Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

```
proyecto_fronda_brick/
├── app/                            # Módulo de Interfaz Web (FastAPI)
│   ├── routers/                  # Endpoints WebSocket y HTTP
│   ├── __init__.py
│   ├── main.py                   # Configuración FastAPI, routers, WebSocket manager
│   ├── connection_manager.py     # Gestión de conexiones WebSocket
│   └── schemas.py                # Pydantic schemas
├── fronda_brick_core/              # Núcleo de Frondabrick y lógica de negocio
│   ├── modulos/                  # Submódulos (aprendizaje, PLN, etc.)
│   ├── persistencia/             # Módulo de Persistencia de Datos (SQLite)
│   ├── fog_manager/              # Módulo de Comunicación en la Niebla (bases)
│   ├── utils/                    # Utilidades compartidas (ej. logging)
│   ├── __init__.py
│   └── fronda_brick.py           # Clase principal FrondaBrick
├── tests/                          # Pruebas (unitarias, integración, E2E)
├── Dockerfile                      # Para la contenerización
├── requirements.txt                # Dependencias de Python
├── frondabrick.db                  # Base de datos SQLite (se crea al ejecutar)
├── arquitectura_frondabrick.md     # Documento de arquitectura
├── diagrama_flujo_errores_frondabrick.md # Documento de flujo y errores
├── todo.md                         # Plan de desarrollo y seguimiento
└── README.md                       # Este archivo
```

## 5. Configuración y Ejecución

### 5.1. Requisitos Previos

*   Python 3.11 o superior.
*   `pip` para instalar dependencias.
*   (Opcional) Docker para ejecución en contenedor.

### 5.2. Instalación de Dependencias

Desde la raíz del directorio `proyecto_fronda_brick`:

```bash
pip install -r requirements.txt
```

### 5.3. Inicialización de la Base de Datos

La base de datos (`frondabrick.db`) y sus tablas se crean automáticamente la primera vez que se ejecuta el módulo de persistencia o la aplicación principal si está configurado para ello. Para una inicialización manual (por ejemplo, para desarrollo o pruebas), puedes ejecutar:

```bash
python fronda_brick_core/persistencia/database.py
```

Esto creará el archivo `frondabrick.db` en la raíz del proyecto si no existe y las tablas necesarias.

### 5.4. Ejecución de la Aplicación (Servidor FastAPI)

Desde la raíz del directorio `proyecto_fronda_brick`:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

*   `--reload`: El servidor se reiniciará automáticamente con los cambios en el código (útil para desarrollo).
*   `--host 0.0.0.0`: Hace que el servidor sea accesible desde otras máquinas en la red local.
*   `--port 8000`: Especifica el puerto en el que se ejecutará el servidor.

Una vez iniciado, puedes acceder a:

*   **Interfaz de prueba WebSocket:** `http://localhost:8000/` (si la ruta raíz en `app/main.py` está habilitada con el HTML de prueba).
*   **Endpoint WebSocket:** `ws://localhost:8000/ws/chat`
*   **Documentación de la API (Swagger UI):** `http://localhost:8000/docs`
*   **Documentación alternativa de la API (ReDoc):** `http://localhost:8000/redoc`

### 5.5. Ejecución con Docker (Próximamente)

El `Dockerfile` está incluido para facilitar la contenerización. Se proporcionarán instrucciones detalladas para construir y ejecutar la imagen de Docker en una futura actualización de este README.

## 6. Logging y Trazabilidad

El sistema implementa un logging exhaustivo para facilitar el seguimiento del comportamiento, la depuración y la monitorización. Los logs se configuran para mostrar información relevante sobre las operaciones, errores y eventos del sistema.

Se están implementando flags de trazabilidad para el modo de desarrollo que permitirán obtener información más detallada.

## 7. Pruebas

El directorio `tests/` contendrá las pruebas unitarias, de integración y end-to-end. La estrategia de pruebas se adhiere al principio de "no mocks" siempre que sea posible, enfocándose en la interacción real entre componentes.

## 8. Contribuciones y Futuras Mejoras

(Sección a detallar en el futuro)

*   Implementación completa del sistema de aprendizaje "Fronda".
*   Desarrollo avanzado de heurísticas.
*   Integración completa con la "Niebla" para computación distribuida.
*   Mejoras en la interfaz de usuario y cliente WebSocket.
*   Seguridad avanzada y autenticación.

## 9. Licencia

(Sección a definir)

