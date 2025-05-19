# app/routers/conversacional.py
import uuid
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from ..connection_manager import ConnectionManager # Relative import
from fronda_brick_core.fronda_brick import FrondaBrick

# Instancia global del núcleo de Frondabrick para toda la app
fronda_core = FrondaBrick()

router = APIRouter()

# This is a global manager, ideally injected or accessed via app state
# For simplicity in this step, we might need to access it from app.main.manager
# A better way would be to use Depends for such shared resources if FastAPI supports it for WebSockets easily
# or pass it around. For now, let's assume we can get it from the app instance or a global.

# To access the manager created in main.py, we might need a dependency or to pass the app instance.
# Let's try to get it from the WebSocket request's app attribute if available, or define it globally for now.
# For now, we will assume 'manager' is accessible. This will be refined.
# from ..main import manager # This creates a circular import if main imports this router.

# A common pattern is to have a dependency that provides the manager
# async def get_connection_manager():
#     # This would typically come from app.state or a global initialized in main
#     # For now, we'll assume it's globally accessible for simplicity of this step
#     from ..main import manager # This is problematic due to potential circular imports
#     return manager

# Let's define a placeholder for the FrondaBrick core instance
# fronda_core = FrondaBrick() # This would be initialized appropriately

@router.websocket("/ws/chat")
async def websocket_endpoint(websocket: WebSocket):
    # This import is here to avoid circular dependency issues at module load time
    # It's not ideal but works for now. Proper dependency injection is better.
    from ..main import manager as global_manager

    client_id = str(uuid.uuid4())
    await global_manager.connect(websocket, client_id)
    await global_manager.send_personal_message(f"Bienvenido, Cliente {client_id}! Estás conectado a Frondabrick.", client_id)
    try:
        while True:
            data = await websocket.receive_text() # Expecting text, could be JSON
            # Procesar el mensaje con la IA FrondaBrick
            core_response = fronda_core.process_message(client_id, data)
            await global_manager.send_personal_message(core_response, client_id)

    except WebSocketDisconnect:
        global_manager.disconnect(client_id)
        # Optionally, notify other clients or log the disconnection
        # await manager.broadcast(f"Cliente {client_id} se ha desconectado.")
        print(f"Cliente {client_id} desconectado")
    except Exception as e:
        # Log the error
        print(f"Error con cliente {client_id}: {e}")
        # Try to send an error message to the client if the connection is still alive
        try:
            await websocket.send_text(f"Ocurrió un error: {str(e)}. Por favor, intenta reconectar.")
        except Exception as e2:
            print(f"No se pudo enviar mensaje de error al cliente {client_id}: {e2}")
        finally:
            global_manager.disconnect(client_id)

