"""
Esquemas de Pydantic para Survey.
"""
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

class SurveyBase(BaseModel):
    title: str
    description: Optional[str] = None

class SurveyCreate(SurveyBase):
    pass

from app.schemas.question import QuestionRead

class SurveyRead(SurveyBase):
    id: int
    created_at: datetime
    questions: List[QuestionRead] = []
    model_config = {
        "from_attributes": True
    }
