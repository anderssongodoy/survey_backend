"""
Archivo principal de la aplicación FastAPI.
"""
from fastapi import FastAPI
from app.api import survey, question, option
from app.core.database import Base, engine

app = FastAPI(title="Survey API")

# Crear automáticamente las tablas en la base de datos al iniciar la app
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(survey.router)
app.include_router(question.router)
app.include_router(option.router)
