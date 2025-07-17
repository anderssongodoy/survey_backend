"""
Repositorio para operaciones de base de datos relacionadas con Question.
"""
from sqlalchemy.orm import Session
from app.models.question import Question

class QuestionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, question: Question) -> Question:
        """Crear una nueva pregunta en la base de datos."""
        self.db.add(question)
        self.db.commit()
        self.db.refresh(question)
        return question

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
