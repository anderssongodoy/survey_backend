"""
Esquemas de Pydantic para Question.
"""
from app.schemas.enums import QuestionType
from pydantic import BaseModel
from typing import List
from app.schemas.option import OptionRead

class QuestionBase(BaseModel):
    text: str
    question_type: QuestionType

class QuestionCreate(QuestionBase):
    pass

class QuestionRead(QuestionBase):
    id: int
    survey_id: int
    options: List[OptionRead] = []
    model_config = {
        "from_attributes": True
    }
