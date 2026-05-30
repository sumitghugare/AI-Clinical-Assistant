from fastapi import APIRouter
from pydantic import BaseModel

from services.llm_service import generate_medical_summary

router = APIRouter(
    prefix="/summary",
    tags=["Summary"]
)


class PatientSymptoms(BaseModel):
    symptoms: str


@router.post("/")
def generate_summary(data: PatientSymptoms):

    result = generate_medical_summary(
        data.symptoms
    )

    return {
        "ai_summary": result
    }