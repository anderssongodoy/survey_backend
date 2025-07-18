"""
Esquemas de Pydantic para Question.
"""
from typing import List, Optional
from pydantic import BaseModel
from enum import Enum

class QuestionType(str, Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"

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
