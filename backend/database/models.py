from sqlalchemy import Column, Integer, String

from database.db import Base


class Patient(Base):

    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)

    age = Column(Integer)

    symptoms = Column(String)

    prediction = Column(String)

    summary = Column(String)