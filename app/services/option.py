"""
Servicio para la lógica de negocio relacionada con Option.
"""
from app.repositories.option import OptionRepository
from app.models.option import Option

class OptionService:
    def __init__(self, repository: OptionRepository):
        self.repository = repository

    def create_option(self, option: Option) -> Option:
        """Lógica para crear una opción (puede incluir validaciones, reglas, etc.)."""
        return self.repository.create(option)

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
