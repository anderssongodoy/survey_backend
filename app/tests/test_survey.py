"""
Tests para el endpoint POST /surveys.
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_survey_success():
    payload = {"title": "Customer Satisfaction", "description": "Survey about customer experience"}
    response = client.post("/surveys/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert "id" in data
    assert "created_at" in data

def test_create_survey_without_description():
    payload = {"title": "Only Title"}
    response = client.post("/surveys/", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["description"] is None

def test_create_survey_missing_title():
    payload = {"description": "No title provided"}
    response = client.post("/surveys/", json=payload)
    assert response.status_code == 422  # Unprocessable Entity
