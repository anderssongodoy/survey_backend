"""
Survey router: endpoints related to surveys.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from app.schemas.survey import SurveyCreate, SurveyRead
from app.models.survey import Survey
from app.repositories.survey import SurveyRepository
from app.services.survey import SurveyService
from app.core.database import SessionLocal
import logging

router = APIRouter(prefix="/surveys", tags=["surveys"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[SurveyRead], summary="List all surveys")
def list_surveys(
    skip: int = Query(0, ge=0, description="Number of items to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max items to return"),
    db: Session = Depends(get_db)
):
    """List all surveys with pagination."""
    surveys = db.query(Survey).offset(skip).limit(limit).all()
    return surveys

@router.post("/", response_model=SurveyRead, status_code=status.HTTP_201_CREATED, summary="Create a new survey")
def create_survey(survey_in: SurveyCreate, db: Session = Depends(get_db)):
    """Endpoint to create a new survey."""
    logger = logging.getLogger("survey")
    repository = SurveyRepository(db)
    service = SurveyService(repository)
    survey = Survey(title=survey_in.title, description=survey_in.description)
    try:
        created = service.create_survey(survey)
        logger.info(f"Survey created: {created.title} (id={created.id})")
        return created
    except Exception as e:
        logger.error(f"Error creating survey: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
