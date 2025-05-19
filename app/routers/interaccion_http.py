# app/routers/interaccion_http.py
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/estado", tags=["estado"])
async def get_estado():
    """Devuelve el estado actual de Frondabrick."""
    # En una implementación real, esto podría obtener información del núcleo de Frondabrick
    return {"estado": "Frondabrick IA operativa", "version": "0.0.1"}

@router.post("/feedback_http", tags=["feedback"])
async def post_feedback(feedback_data: dict):
    """
    Permite a los usuarios enviar feedback sobre Frondabrick a través de HTTP.
    Ejemplo de payload: {"user_id": "user123", "rating": 5, "comment": "Excelente IA!"}
    """
    print(f"Feedback recibido vía HTTP: {feedback_data}")
    # Aquí se procesaría el feedback, por ejemplo, guardándolo en la base de datos
    # o enviándolo a un sistema de seguimiento.
    if not feedback_data.get("comment"):
        raise HTTPException(status_code=400, detail="El comentario no puede estar vacío.")
    return {"mensaje": "Feedback recibido correctamente", "datos": feedback_data}

