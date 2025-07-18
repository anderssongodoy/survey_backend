"""
Esquemas de Pydantic para Question.
"""
from app.schemas.enums import QuestionType
from pydantic import BaseModel

class QuestionBase(BaseModel):
    text: str
    question_type: QuestionType

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    survey_id: int
    model_config = {
        "from_attributes": True
    }
