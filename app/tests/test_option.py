"""
Tests para el endpoint POST /questions/{question_id}/options.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def create_survey():
    payload = {"title": "Encuesta para opciones"}
    response = client.post("/surveys/", json=payload)
    assert response.status_code == 201
    return response.json()["id"]

def create_question(survey_id, question_type="single_choice"):
    payload = {"text": "Pregunta con opciones", "question_type": question_type}
    response = client.post(f"/surveys/{survey_id}/questions/", json=payload)
    assert response.status_code == 201
    return response.json()["id"]

def test_add_option_success():
    survey_id = create_survey()
    question_id = create_question(survey_id, question_type="single_choice")
    payload = {"text": "Muy satisfecho"}
    response = client.post(f"/questions/{question_id}/options/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["text"] == payload["text"]
    assert data["question_id"] == question_id

def test_add_option_to_text_question():
    survey_id = create_survey()
    question_id = create_question(survey_id, question_type="text")
    payload = {"text": "No debería permitir"}
    response = client.post(f"/questions/{question_id}/options/", json=payload)
    assert response.status_code == 400

def test_add_option_to_nonexistent_question():
    payload = {"text": "Opción sin pregunta"}
    response = client.post(f"/questions/99999/options/", json=payload)
    assert response.status_code == 404
