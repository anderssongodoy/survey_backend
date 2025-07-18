
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.database import SessionLocal, Base, engine
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

@pytest.fixture(autouse=True)
def setup_and_teardown():
    # Crear las tablas y limpiar antes de cada test
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

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

def test_get_surveys():
    db = SessionLocal()
    survey = create_sample_survey(db)
    db.close()
    response = client.get("/surveys")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert any(s["id"] == survey.id for s in data)

def test_get_survey_by_id():
    db = SessionLocal()
    survey = create_sample_survey(db)
    question = create_sample_question(db, survey.id)
    option = create_sample_option(db, question.id)
    db.close()
    response = client.get(f"/surveys/{survey.id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == survey.id
    assert any(q["id"] == question.id for q in data["questions"])
    assert any(o["id"] == option.id for o in data["questions"][0]["options"])

def test_get_survey_by_id_not_found():
    response = client.get("/surveys/9999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Survey not found"
