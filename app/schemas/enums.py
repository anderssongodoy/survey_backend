from enum import Enum

class QuestionType(str, Enum):
    text = "text"
    single_choice = "single_choice"
    multiple_choice = "multiple_choice"