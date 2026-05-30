from sqlalchemy.orm import Session

from models.consultation import ConsultationNote


def save_consultation_note(
    db: Session,
    patient_id: int,
    note: str
):

    consultation = ConsultationNote(

        patient_id=patient_id,

        note=note
    )

    db.add(consultation)

    db.commit()

    db.refresh(consultation)

    return consultation


def get_patient_notes(
    db: Session,
    patient_id: int
):

    notes = db.query(
        ConsultationNote
    ).filter(

        ConsultationNote.patient_id == patient_id

    ).order_by(

        ConsultationNote.created_at.desc()

    ).all()

    return notes