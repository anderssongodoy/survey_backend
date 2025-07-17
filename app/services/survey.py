"""
Servicio para la lógica de negocio relacionada con Survey.
"""
from app.repositories.survey import SurveyRepository
from app.models.survey import Survey

class SurveyService:
    def __init__(self, repository: SurveyRepository):
        self.repository = repository

    def create_survey(self, survey: Survey) -> Survey:
        """Lógica para crear una encuesta (puede incluir validaciones, reglas, etc.)."""
        return self.repository.create(survey)

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
