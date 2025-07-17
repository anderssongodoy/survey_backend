"""
Router de Survey: endpoints relacionados con encuestas.
"""
from fastapi import APIRouter

router = APIRouter(prefix="/surveys", tags=["surveys"])

@router.post("/", summary="Crear una nueva encuesta")
def create_survey():
    """Endpoint para crear una nueva encuesta (implementación pendiente)."""
    return {"message": "Survey creation endpoint (to be implemented)"}
