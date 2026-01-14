from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_script(idea: str, seconds: int):
    prompt = f"""
Create a short motivational video script.

Topic: {idea}
Duration: {seconds} seconds

Return:
- Scene-wise narration
- Each scene 1–2 lines
- Powerful, cinematic tone
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
