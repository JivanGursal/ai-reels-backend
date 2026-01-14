# scene_service.py
from app.services.runway_service import generate_visual_clip

def generate_scenes(script: str):
    sentences = script.split(".")
    clips = []

    for i, s in enumerate(sentences):
        if len(s.strip()) < 5:
            continue

        clip_path = generate_visual_clip(
            prompt=f"cinematic scene, {s}, ultra realistic, 9:16",
            duration=5
        )
        clips.append(clip_path)

    return clips
