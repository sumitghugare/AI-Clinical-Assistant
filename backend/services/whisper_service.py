import whisper
import os

# Load Whisper model once
model = whisper.load_model("base")


def transcribe_audio(audio_path: str):

    try:
        result = model.transcribe(audio_path)

        text = result["text"]

        return {
            "success": True,
            "transcription": text
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }