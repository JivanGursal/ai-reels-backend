from app.services.groq_service import generate_text

LANGUAGE_MAP = {
    "english": "English",
    "hindi": "Hindi",
    "marathi": "Marathi",
    "gujarati": "Gujarati",
    "kannada": "Kannada",
    "tamil": "Tamil",
    "rajasthani": "Rajasthani"
}


def generate_script(topic: str, language: str, seconds: int) -> str:
    lang = LANGUAGE_MAP.get(language, "English")

    prompt = f"""
You are a professional motivational reel script writer.

Language: {lang}
Topic: "{topic}"
Duration: {seconds} seconds

Rules:
- Short cinematic lines
- Emotional & motivational
- No titles, no markdown
- Spoken narration only
"""

    return generate_text(prompt)
