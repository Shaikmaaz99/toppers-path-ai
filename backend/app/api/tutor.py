from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.ai import ask_tutor

router = APIRouter(prefix="/api/tutor", tags=["AI Tutor"])


class TutorRequest(BaseModel):
    question: str


@router.post("/chat")
def tutor_chat(request: TutorRequest):
    answer = ask_tutor(request.question)

    return {
        "question": request.question,
        "answer": answer
    }
