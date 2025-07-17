"""
Router de Option: endpoints relacionados con opciones de respuesta.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/questions/{question_id}/options", tags=["options"])

@router.post("/", summary="Agregar una opción a una pregunta")
def add_option(question_id: int):
    """Endpoint para agregar una opción a una pregunta (implementación pendiente)."""
    return {"message": "Add option endpoint (to be implemented)", "question_id": question_id}
