from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_medical_summary

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)


class ChatRequest(BaseModel):
    message: str


@router.post("/")
def chatbot(data: ChatRequest):

    result = generate_medical_summary(
        data.message
    )

    return {
        "response": result
    }