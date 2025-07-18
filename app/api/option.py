"""
Option router: endpoints related to answer options.
"""
from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from app.schemas.option import OptionCreate, OptionRead
from app.models.option import Option
from app.models.question import Question, QuestionType
from app.repositories.option import OptionRepository
from app.services.option import OptionService
from app.repositories.question import QuestionRepository
from app.core.database import SessionLocal
import logging

router = APIRouter(prefix="/questions/{question_id}/options", tags=["options"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=OptionRead, status_code=status.HTTP_201_CREATED, summary="Add an option to a question")
def add_option(
    question_id: int = Path(..., description="ID of the question"),
    option_in: OptionCreate = None,
    db: Session = Depends(get_db)
):
    """Endpoint to add an option to a question."""
    logger = logging.getLogger("option")
    # Validar que la pregunta existe
    question_repo = QuestionRepository(db)
    question = db.query(Question).filter_by(id=question_id).first()
    if not question:
        logger.warning(f"Question not found: {question_id}")
        raise HTTPException(status_code=404, detail="Question not found")
    # Validar tipo de pregunta
    if question.question_type not in [QuestionType.single_choice, QuestionType.multiple_choice]:
        logger.warning(f"Options only allowed for single_choice or multiple_choice questions. Question id: {question_id}")
        raise HTTPException(status_code=400, detail="Options only allowed for single_choice or multiple_choice questions")
    repo = OptionRepository(db)
    service = OptionService(repo)
    option = Option(
        text=option_in.text,
        question_id=question_id
    )
    try:
        created = service.create_option(option)
        logger.info(f"Option created: {created.text} (id={created.id}) for question {question_id}")
        return created
    except Exception as e:
        logger.error(f"Error creating option: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
