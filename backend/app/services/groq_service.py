import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(topic: str, seconds: int, language: str):
    prompt = f"""
Write a cinematic motivational video script.

Language: {language}
Topic: {topic}
Duration: {seconds} seconds

Rules:
- Scene-wise narration
- Each scene 1–2 powerful lines
- Emotional, bold tone
- Only narration text
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
