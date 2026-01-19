import os
from groq import Groq

def generate_script(idea: str, seconds: int) -> str:
    """
    Generates a cinematic motivational script using Groq LLM.
    SAFE for Render + background workers.
    """

    if not idea or seconds <= 0:
        return "Stay focused. Discipline creates success."

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    prompt = f"""
You are a professional motivational video script writer.

Create a powerful, cinematic script for a short video.

Topic: "{idea}"
Total Duration: {seconds} seconds

Rules:
- Divide into clear scenes
- Each scene: 1–2 short impactful lines
- No markdown
- No titles
- Only narration text
- Motivational, bold, emotional tone
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        script = response.choices[0].message.content.strip()
        return script or "Discipline today builds freedom tomorrow."

    except Exception as e:
        # Render / worker safe fallback
        return "Greatness is built one disciplined step at a time."
