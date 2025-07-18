"""
Question router: endpoints related to questions.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from app.schemas.question import QuestionCreate, QuestionRead
from app.models.question import Question, QuestionType
from app.repositories.question import QuestionRepository
from app.services.question import QuestionService
from app.repositories.survey import SurveyRepository
from app.core.database import SessionLocal
import logging

router = APIRouter(prefix="/surveys/{survey_id}/questions", tags=["questions"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=QuestionRead, status_code=status.HTTP_201_CREATED, summary="Add a question to a survey")
def add_question(
    survey_id: int = Path(..., description="ID of the survey"),
    question_in: QuestionCreate = None,
    db: Session = Depends(get_db)
):
    """Endpoint to add a question to a survey."""
    logger = logging.getLogger("question")
    # Validar que la encuesta existe
    survey_repo = SurveyRepository(db)
    survey = survey_repo.get_by_id(survey_id)
    if not survey:
        logger.warning(f"Survey not found: {survey_id}")
        raise HTTPException(status_code=404, detail="Survey not found")
    # Validar tipo de pregunta
    if question_in.question_type not in QuestionType.__members__.values():
        logger.warning(f"Invalid question type: {question_in.question_type}")
        raise HTTPException(status_code=400, detail="Invalid question type")
    repo = QuestionRepository(db)
    service = QuestionService(repo)
    question = Question(
        text=question_in.text,
        question_type=question_in.question_type,
        survey_id=survey_id
    )
    try:
        created = service.create_question(question)
        logger.info(f"Question created: {created.text} (id={created.id}) for survey {survey_id}")
        return created
    except Exception as e:
        logger.error(f"Error creating question: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
