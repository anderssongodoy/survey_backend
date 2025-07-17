"""
Servicio para la lógica de negocio relacionada con Question.
"""
from app.repositories.question import QuestionRepository
from app.models.question import Question

class QuestionService:
    def __init__(self, repository: QuestionRepository):
        self.repository = repository

    def create_question(self, question: Question) -> Question:
        """Lógica para crear una pregunta (puede incluir validaciones, reglas, etc.)."""
        return self.repository.create(question)

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
