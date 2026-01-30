import os, replicate, uuid
from app.core.config import settings

replicate.Client(api_token=settings.REPLICATE_API_TOKEN)

def generate_images(prompts: list[str]) -> list[str]:
    images = []

    for p in prompts:
        output = replicate.run(
            "stability-ai/sdxl",
            input={"prompt": p}
        )
        path = f"{settings.VISUAL_DIR}/{uuid.uuid4().hex}.png"
        with open(path, "wb") as f:
            f.write(output[0])
        images.append(path)

    return images
