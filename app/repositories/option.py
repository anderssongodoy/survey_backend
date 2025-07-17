"""
Repositorio para operaciones de base de datos relacionadas con Option.
"""
from sqlalchemy.orm import Session
from app.models.option import Option

class OptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, option: Option) -> Option:
        """Crear una nueva opción en la base de datos."""
        self.db.add(option)
        self.db.commit()
        self.db.refresh(option)
        return option

    # Métodos adicionales (get, list, etc.) pueden agregarse aquí
