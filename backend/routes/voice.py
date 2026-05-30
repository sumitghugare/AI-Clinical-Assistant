from fastapi import APIRouter, UploadFile, File
import shutil
import os

from services.whisper_service import transcribe_audio

router = APIRouter()

TEMP_DIR = "temp_audio"

# Create temp folder automatically
os.makedirs(TEMP_DIR, exist_ok=True)


@router.post("/transcribe")

async def transcribe_voice(file: UploadFile = File(...)):

    try:

        # File path
        file_path = os.path.join(TEMP_DIR, file.filename)

        # Save uploaded audio
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Transcribe audio
        result = transcribe_audio(file_path)

        # Delete temp file after processing
        os.remove(file_path)

        return result

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }