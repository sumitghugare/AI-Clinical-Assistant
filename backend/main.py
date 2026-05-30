from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.voice import router as voice_router
# from routes.predict import router as predict_router
from routes.consultation import router as consultation_router
from routes.consultation import router as consultation_router

from routes import (
    prediction,
    summary,
    transcription,
    report,
    chatbot,
    auth,
    patients
)

from database.db import engine
from database.models import Base

# CREATE DATABASE TABLES
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Clinical Assistant",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTES
app.include_router(prediction.router)
app.include_router(summary.router)
app.include_router(transcription.router)
app.include_router(report.router)
app.include_router(chatbot.router)
app.include_router(auth.router)
app.include_router(patients.router)
app.include_router(voice_router)
# app.include_router(predict_router)
app.include_router(voice_router)
app.include_router(consultation_router)
app.include_router(consultation_router)


@app.get("/")
def home():

    return {
        "message": "AI Clinical Assistant Running Successfully"
    }