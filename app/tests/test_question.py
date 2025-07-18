"""
Tests para el endpoint POST /surveys/{survey_id}/questions.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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
