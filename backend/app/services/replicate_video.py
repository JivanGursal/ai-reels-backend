import replicate
import uuid
import os
from app.core.config import settings

replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

def generate_video_from_image(image_path: str, prompt: str) -> str:
    output = replicate.run(
        "stability-ai/stable-video-diffusion",
        input={
            "input_image": open(image_path, "rb"),
            "prompt": prompt
        }
    )

    path = os.path.join(
        settings.VIDEO_DIR,
        f"clip_{uuid.uuid4().hex}.mp4"
    )

    with open(path, "wb") as f:
        f.write(output)

    return path
