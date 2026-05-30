from mistralai import Mistral
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

client = Mistral(api_key=api_key)


def generate_medical_summary(symptoms):

    prompt = f"""
    You are an AI medical assistant.

    Analyze these symptoms and generate:

    1. Short medical summary
    2. Possible health concern
    3. Basic recommendation

    Symptoms:
    {symptoms}
    """

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content