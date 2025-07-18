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

class SurveyRead(SurveyBase):
    id: int
    created_at: datetime
    model_config = {
        "from_attributes": True
    }
