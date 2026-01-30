import requests, uuid, os
from app.core.config import settings

def generate_voice(text: str, language: str):
    headers = {
        "xi-api-key": settings.ELEVENLABS_API_KEY,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {"stability": 0.4, "similarity_boost": 0.8}
    }

    res = requests.post(
        "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM",
        headers=headers,
        json=payload
    )

    path = f"{settings.AUDIO_DIR}/voice_{uuid.uuid4().hex}.mp3"
    with open(path, "wb") as f:
        f.write(res.content)

    return path
