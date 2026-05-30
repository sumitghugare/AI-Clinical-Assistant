from fastapi import APIRouter

from database.db import SessionLocal
from database.models import Patient

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.get("/")
def get_all_patients():

    db = SessionLocal()

    patients = db.query(Patient).all()

    result = []

    for patient in patients:

        result.append({
            "id": patient.id,
            "name": patient.name,
            "age": patient.age,
            "symptoms": patient.symptoms,
            "prediction": patient.prediction,
            "summary": patient.summary
        })

    db.close()

    return {
        "patients": result
    }