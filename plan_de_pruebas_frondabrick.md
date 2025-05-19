# Plan de Pruebas para Frondabrick v0.01

## 1. Introducción

Este documento describe la estrategia y el plan de pruebas para validar el funcionamiento, la robustez y la escalabilidad básica de Frondabrick v0.01. Las pruebas se realizarán adhiriéndose al principio de "no mocks", utilizando componentes reales e interacciones end-to-end siempre que sea posible.

## 2. Objetivos de las Pruebas

*   Verificar que la funcionalidad conversacional a través de WebSockets opera correctamente.
*   Validar la correcta persistencia y recuperación de datos (conocimiento, reglas, historial) en la base de datos SQLite.
*   Probar la funcionalidad básica del sistema de aprendizaje "Fronda".
*   Evaluar el rendimiento del núcleo de Frondabrick y la capacidad del servidor WebSocket para manejar múltiples conexiones concurrentes (pruebas básicas).
*   Asegurar que el manejo de errores es robusto y proporciona la retroalimentación adecuada.
*   Confirmar que el sistema de logging registra la información necesaria para la depuración y monitorización.

## 3. Alcance de las Pruebas

### 3.1. Pruebas de Funcionalidad Conversacional (End-to-End)

*   **Conexión y Desconexión WebSocket:**
    *   Establecer múltiples conexiones WebSocket simultáneas.
    *   Verificar mensajes de bienvenida y gestión de ID de cliente.
    *   Probar desconexiones limpias y abruptas, y verificar la limpieza de recursos en el servidor.
*   **Intercambio de Mensajes:**
    *   Enviar mensajes simples y verificar respuestas predefinidas del núcleo (ej. "hola", "estado").
    *   Enviar mensajes que deberían activar la lógica de aprendizaje (placeholder).
    *   Probar el envío de mensajes con formatos válidos e inválidos (si se definen esquemas estrictos para el contenido del mensaje WebSocket).
*   **Manejo de Múltiples Clientes:**
    *   Asegurar que las conversaciones de diferentes clientes se mantienen aisladas y con el contexto correcto.

### 3.2. Pruebas de Persistencia de Datos (Integración)

*   **Conocimiento:**
    *   Añadir, recuperar, actualizar y eliminar entradas de conocimiento a través de interacciones que disparen estas operaciones en el núcleo (o mediante funciones de prueba directas del módulo CRUD si es necesario para una cobertura completa).
    *   Verificar que los datos se almacenan y recuperan correctamente de `frondabrick.db`.
*   **Reglas:**
    *   Añadir y recuperar reglas (la funcionalidad de actualización y eliminación puede ser menos prioritaria para v0.01 si no está completamente implementada en el núcleo).
    *   Verificar almacenamiento en `frondabrick.db`.
*   **Historial de Conversaciones:**
    *   Verificar que cada interacción (mensaje de usuario y respuesta de IA) se registra correctamente en la tabla `historial_conversaciones` con el `client_id` correcto.
    *   Recuperar el historial de un cliente específico.

### 3.3. Pruebas del Sistema de Aprendizaje (Integración/Funcional)

*   Enviar mensajes diseñados para activar la funcionalidad de aprendizaje (actualmente placeholders en el núcleo).
*   Verificar que el núcleo invoca (o intentaría invocar) las funciones de aprendizaje correspondientes.
*   Verificar que los datos (simulados) de aprendizaje se intentan persistir (ej. se llama a `crud.add_knowledge`).
*   **Nota:** Dado que el aprendizaje es básico en v0.01, las pruebas se centrarán en la invocación y el flujo, más que en la efectividad del aprendizaje en sí.

### 3.4. Pruebas de Manejo de Errores

*   Enviar mensajes malformados al endpoint WebSocket.
*   Simular errores en la base de datos (si es posible sin mocks, ej. intentando insertar datos duplicados que violen constraints UNIQUE) y verificar la respuesta del sistema.
*   Probar desconexiones inesperadas de clientes.
*   Revisar logs para asegurar que los errores se registran adecuadamente.

### 3.5. Pruebas de Logging

*   Ejecutar varios escenarios de prueba y revisar los archivos de log (o salida de consola) para confirmar:
    *   Registro de conexiones y desconexiones WebSocket.
    *   Registro de mensajes recibidos y enviados.
    *   Registro de operaciones de base de datos (si se implementa logging en el módulo CRUD).
    *   Registro de errores y excepciones.
    *   Funcionamiento de flags de trazabilidad (si se implementan para modo desarrollo).

### 3.6. Pruebas de Rendimiento y Escalabilidad Básica (Consideraciones)

*   Conectar un número moderado de clientes WebSocket simultáneos (ej. 5-10) y realizar interacciones básicas para observar la respuesta del servidor.
*   Monitorear el uso de CPU y memoria del proceso del servidor bajo esta carga ligera.
*   **Nota:** No se realizarán pruebas de carga exhaustivas para v0.01, pero se observará el comportamiento general.

## 4. Entorno de Pruebas

*   **Sistema Operativo:** El mismo entorno de desarrollo (Linux sandbox).
*   **Base de Datos:** Instancia local de SQLite (`frondabrick.db`).
*   **Cliente WebSocket:** Se puede usar una herramienta de cliente WebSocket (como una extensión de navegador, Postman, o un script simple en Python con la biblioteca `websockets`) o la página HTML de prueba en `http://localhost:8000/`.

## 5. Procedimiento de Prueba

1.  **Preparación:**
    *   Asegurar que el código fuente está actualizado.
    *   Instalar todas las dependencias (`pip install -r requirements.txt`).
    *   Asegurar que la base de datos `frondabrick.db` está limpia o en un estado conocido (puede ser necesario eliminarla y reiniciarla con `python fronda_brick_core/persistencia/database.py` antes de cada ciclo de pruebas importante).
    *   Iniciar el servidor Frondabrick: `uvicorn app.main:app --reload --host 0.0.0.0 --port 8000`.
2.  **Ejecución de Casos de Prueba:**
    *   Seguir los escenarios definidos en la sección 3.
    *   Para cada caso, registrar los pasos realizados, los resultados esperados y los resultados observados.
    *   Revisar los logs del servidor y el contenido de la base de datos SQLite según sea necesario.
3.  **Registro de Defectos:**
    *   Cualquier discrepancia entre el resultado esperado y el observado se registrará como un defecto, incluyendo pasos para reproducirlo, logs relevantes y severidad.
4.  **Informe de Pruebas:**
    *   Al finalizar el ciclo de pruebas, se generará un resumen de los resultados.

## 6. Criterios de Aceptación (para v0.01)

*   Todas las funcionalidades principales (conversación básica, persistencia de historial) operan como se espera.
*   El sistema es estable bajo interacciones normales.
*   Los errores se manejan de forma controlada y se registran.
*   La documentación de logs es suficiente para el diagnóstico básico.

## 7. Casos de Prueba Específicos (Ejemplos a detallar durante la ejecución)

*   **TC001: Conexión WebSocket Exitosa**
*   **TC002: Envío y Recepción de Mensaje Simple ("hola")**
*   **TC003: Persistencia de Historial de Conversación**
*   **TC004: Intento de Aprendizaje (Verificación de Flujo)**
*   **TC005: Manejo de Mensaje Malformado (si aplica esquema estricto)**
*   **TC006: Conexión de Múltiples Clientes Simultáneos (2-3 clientes)**

Este plan se actualizará a medida que avance el desarrollo y las pruebas.
