import os
import requests
from app.utils.files import unique_filename

ELEVEN_URL = "https://api.elevenlabs.io/v1/text-to-speech"


VOICE_MAP = {
    "english": "Rachel",
    "hindi": "Prem",
    "marathi": "Prem",
    "gujarati": "Prem",
    "kannada": "Prem",
    "tamil": "Prem",
    "rajasthani": "Prem"
}


def generate_voice(text: str, language: str, output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)

    voice = VOICE_MAP.get(language, "Rachel")
    filename = unique_filename("voice", "mp3")
    path = os.path.join(output_dir, filename)

    headers = {
        "xi-api-key": os.getenv("ELEVENLABS_API_KEY"),
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.6,
            "similarity_boost": 0.8
        }
    }

    r = requests.post(
        f"{ELEVEN_URL}/{voice}",
        json=payload,
        headers=headers
    )

    with open(path, "wb") as f:
        f.write(r.content)

    return path
