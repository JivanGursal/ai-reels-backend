from app.services.groq_service import generate_script as _generate

def generate_script(idea: str, seconds: int, language: str = "English") -> str:
    return _generate(idea, seconds, language)
