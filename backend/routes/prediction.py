from fastapi import APIRouter
from pydantic import BaseModel

from database.db import SessionLocal
from database.models import Patient

from services.ml_service import predict_heart_risk

router = APIRouter(
    prefix="/prediction",
    tags=["Prediction"]
)


class PatientData(BaseModel):

    name: str
    age: int
    gender: str
    weight: float
    height: float
    smoking: str
    diabetes: str
    cholesterol: float
    blood_pressure: float
    chest_pain: str
    symptoms: str


@router.post("/")
def predict(data: PatientData):

    patient_data = data.dict()

    # ML PREDICTION
    risk = predict_heart_risk(
        patient_data
    )

    # DATABASE SESSION
    db = SessionLocal()

    # SAVE PATIENT
    patient = Patient(
        name=data.name,
        age=data.age,
        symptoms=data.symptoms,
        prediction=risk,
        summary="Pending"
    )

    db.add(patient)

    db.commit()

    db.refresh(patient)

    db.close()

    return {
        "heart_risk": risk
    }