from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from database.db import SessionLocal

from services.consultation_service import (
    save_consultation_note,
    get_patient_notes
)

router = APIRouter()


# =====================================================
# DATABASE SESSION
# =====================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


# =====================================================
# SAVE CONSULTATION NOTE
# =====================================================

@router.post("/consultation/add")

def add_consultation_note(
    data: dict,
    db: Session = Depends(get_db)
):

    note = save_consultation_note(

        db=db,

        patient_id=data["patient_id"],

        note=data["note"]
    )

    return {
        "message": "Consultation note saved successfully"
    }


# =====================================================
# GET CONSULTATION HISTORY
# =====================================================

@router.get("/consultation/{patient_id}")

def fetch_patient_notes(
    patient_id: int,
    db: Session = Depends(get_db)
):

    notes = get_patient_notes(
        db,
        patient_id
    )

    result = []

    for note in notes:

        result.append({

            "note": note.note,

            "created_at": note.created_at
        })

    return {
        "notes": result
    }