"""
Tests para el endpoint POST /surveys/{survey_id}/questions.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal
from app.models.survey import Survey
from app.models.question import Question
from app.models.option import Option
from app.schemas.enums import QuestionType
from sqlalchemy.orm import Session

client = TestClient(app)

def create_sample_survey(db: Session):
    survey = Survey(title="Encuesta de prueba", description="Descripción de prueba")
    db.add(survey)
    db.commit()
    db.refresh(survey)
    return survey

def create_sample_question(db: Session, survey_id: int):
    question = Question(text="¿Cuál es tu color favorito?", question_type=QuestionType.single_choice.value, survey_id=survey_id)
    db.add(question)
    db.commit()
    db.refresh(question)
    return question

def create_sample_option(db: Session, question_id: int):
    option = Option(text="Azul", question_id=question_id)
    db.add(option)
    db.commit()
    db.refresh(option)
    return option

def create_survey():
    payload = {"title": "Encuesta para preguntas"}
    response = client.post("/surveys/", json=payload)
    assert response.status_code == 201
    return response.json()["id"]

def test_add_question_success():
    survey_id = create_survey()
    payload = {"text": "¿Cómo calificarías el servicio?", "question_type": "single_choice"}
    response = client.post(f"/surveys/{survey_id}/questions/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == payload["text"]
    assert data["question_type"] == payload["question_type"]
    assert data["survey_id"] == survey_id

def test_add_question_invalid_type():
    survey_id = create_survey()
    payload = {"text": "Pregunta inválida", "question_type": "invalid_type"}
    response = client.post(f"/surveys/{survey_id}/questions/", json=payload)
    assert response.status_code == 422 or response.status_code == 400

def test_add_question_to_nonexistent_survey():
    payload = {"text": "Pregunta sin encuesta", "question_type": "text"}
    response = client.post(f"/surveys/99999/questions/", json=payload)
    assert response.status_code == 404

def test_get_question_by_id():
    db = SessionLocal()
    survey = create_sample_survey(db)
    question = create_sample_question(db, survey.id)
    option = create_sample_option(db, question.id)

    question_id = question.id
    option_id = option.id
    db.close()

    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == question_id
    assert any(o["id"] == option_id for o in data["options"])

def test_get_question_by_id_not_found():
    response = client.get("/questions/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Question not found"
