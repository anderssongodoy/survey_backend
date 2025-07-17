"""
Router de Question: endpoints relacionados con preguntas.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/surveys/{survey_id}/questions", tags=["questions"])

@router.post("/", summary="Agregar una pregunta a una encuesta")
def add_question(survey_id: int):
    """Endpoint para agregar una pregunta a una encuesta (implementación pendiente)."""
    return {"message": "Add question endpoint (to be implemented)", "survey_id": survey_id}
