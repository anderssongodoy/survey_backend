"""
Repositorio para operaciones de base de datos relacionadas con Survey.
"""
from sqlalchemy.orm import Session
from app.models.survey import Survey

class SurveyRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, survey: Survey) -> Survey:
        """Crear una nueva encuesta en la base de datos."""
        self.db.add(survey)
        self.db.commit()
        self.db.refresh(survey)
        return survey

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
