from fastapi import APIRouter

router = APIRouter(
    prefix="/transcription",
    tags=["Transcription"]
)


@router.get("/")
def transcription_home():

    return {
        "message": "Whisper Transcription Route"
    }