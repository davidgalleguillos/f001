# app/main.py
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse # For a simple test page
from typing import List

from .routers import conversacional, interaccion_http
from .connection_manager import ConnectionManager

app = FastAPI(
    title="Frondabrick AI",
    version="0.0.1",
    description="IA avanzada y modular con capacidad de aprendizaje autónomo avanzado."
)

manager = ConnectionManager()

# Incluir routers
app.include_router(conversacional.router)
app.include_router(interaccion_http.router)

@app.get("/")
async def get_root():
    # Simple HTML page to test WebSocket connection if needed directly from browser
    return HTMLResponse("""
    <h1>Frondabrick WebSocket Tester</h1>
    <p>Connect to /ws/chat</p>
    <button onclick="fetchHistorial()" style='margin-bottom:10px;'>Ver Historial</button>
    <div id='historial' style='max-height:180px;overflow:auto;font-size:0.95em;margin-bottom:10px;'></div>
    <script>
        var ws = new WebSocket("ws://localhost:8000/ws/chat");
        ws.onmessage = function(event) {
            var messages = document.getElementById('messages')
            var message = document.createElement('li')
            var content = document.createTextNode(event.data)
            message.appendChild(content)
            messages.appendChild(message)
        };
        function sendMessage(event) {
            var input = document.getElementById("messageText")
            ws.send(input.value)
            input.value = ''
            event.preventDefault()
        }
        function fetchHistorial() {
            // Obtener el client_id actual del primer mensaje de bienvenida, si existe
            var clientId = null;
            var messages = document.getElementById('messages');
            if (messages && messages.children.length > 0) {
                var welcome = messages.children[0].textContent;
                var match = welcome && welcome.match(/Cliente ([\w\-]+)/);
                if (match) clientId = match[1];
            }
            if (!clientId) {
                alert('Primero debes conectarte y recibir el mensaje de bienvenida.');
                return;
            }
            fetch('/historial/' + clientId)
                .then(r => r.json())
                .then(data => {
                    var historialDiv = document.getElementById('historial');
                    if (!data.historial || data.historial.length === 0) {
                        historialDiv.innerHTML = '<em>Sin historial para este cliente.</em>';
                        return;
                    }
                    var html = '<ul style="padding-left:16px">';
                    data.historial.reverse().forEach(function(item) {
                        html += '<li><b>Yo:</b> ' + item.mensaje_usuario + '<br><b>Fronda:</b> ' + item.respuesta_ia + '</li>';
                    });
                    html += '</ul>';
                    historialDiv.innerHTML = html;
                })
                .catch(() => {
                    document.getElementById('historial').innerHTML = '<em>Error al obtener historial.</em>';
                });
        }
    </script>
    <ul id='messages'></ul>
    <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="messageText" autocomplete="off"/>
        <button>Send</button>
    </form>
    """)

# El endpoint WebSocket principal se define en routers/conversacional.py
# y utiliza el 'manager' global definido aquí.

if __name__ == "__main__":
    import uvicorn
    # Esta ejecución es solo para desarrollo local directo del archivo.
    # Para producción o ejecución con Docker, se usará un comando uvicorn diferente.
    uvicorn.run(app, host="0.0.0.0", port=8000)


