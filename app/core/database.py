"""
Configuración de la conexión a la base de datos PostgreSQL usando SQLAlchemy.
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# URL de conexión a la base de datos (ajustar según entorno)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/survey_db")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
