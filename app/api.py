from fastapi import APIRouter
from pydantic import BaseModel
from app.qa_engine import answer_question

router = APIRouter()

class QARequest(BaseModel):
    question: str
    context: str = None  # Optional

@router.post("/qa")
def get_answer(payload: QARequest):
    answer = answer_question(payload.question, payload.context)
    return {"answer": answer}
