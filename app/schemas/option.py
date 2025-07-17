"""
Esquemas de Pydantic para Option.
"""
from pydantic import BaseModel

class OptionBase(BaseModel):
    text: str

class OptionCreate(OptionBase):
    pass

class OptionRead(OptionBase):
    id: int
    question_id: int
    class Config:
        orm_mode = True
