"""
Archivo principal de la aplicación FastAPI.
"""
from fastapi import FastAPI
from app.api import survey, question, option

app = FastAPI(title="Survey API")

# Incluir routers
app.include_router(survey.router)
app.include_router(question.router)
app.include_router(option.router)
