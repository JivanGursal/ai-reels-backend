import os
import uuid
import time
import requests

RUNWAY_API_KEY = os.getenv("RUNWAY_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {RUNWAY_API_KEY}",
    "Content-Type": "application/json"
}

def generate_visual_clip(prompt: str, duration: int = 6) -> str:
    """
    Generates AI video clip using Runway
    Returns local file path
    """

    # 1️⃣ Create generation task
    res = requests.post(
        "https://api.runwayml.com/v1/video/generations",
        headers=HEADERS,
        json={
            "model": "gen-3",
            "prompt": prompt,
            "duration": duration,
            "ratio": "9:16"
        }
    )
    res.raise_for_status()
    task_id = res.json()["id"]

    # 2️⃣ Poll until ready
    while True:
        status = requests.get(
            f"https://api.runwayml.com/v1/video/generations/{task_id}",
            headers=HEADERS
        ).json()

        if status["status"] == "completed":
            video_url = status["output"]["video"]
            break

        if status["status"] == "failed":
            raise Exception("Runway generation failed")

        time.sleep(3)

    # 3️⃣ Download video
    os.makedirs("backend/output/visuals", exist_ok=True)
    filename = f"visual_{uuid.uuid4().hex}.mp4"
    filepath = f"backend/output/visuals/{filename}"

    video_data = requests.get(video_url).content
    with open(filepath, "wb") as f:
        f.write(video_data)

    return filepath
