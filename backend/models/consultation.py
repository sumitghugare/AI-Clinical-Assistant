from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from datetime import datetime

from database.db import Base


class ConsultationNote(Base):

    __tablename__ = "consultation_notes"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    patient_id = Column(
        Integer,
        ForeignKey("patients.id")
    )

    note = Column(
        String
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )