import os
import replicate
from app.utils.files import unique_filename

replicate.Client(api_token=os.getenv("REPLICATE_API_TOKEN"))


def generate_images(script: str, count: int, output_dir: str) -> list[str]:
    os.makedirs(output_dir, exist_ok=True)
    images = []

    prompt = f"Cinematic motivational visuals. {script}"

    output = replicate.run(
        "stability-ai/sdxl",
        input={
            "prompt": prompt,
            "num_outputs": count,
            "aspect_ratio": "9:16"
        }
    )

    for img_url in output:
        filename = unique_filename("scene", "png")
        path = os.path.join(output_dir, filename)

        import requests
        img_data = requests.get(img_url).content
        with open(path, "wb") as f:
            f.write(img_data)

        images.append(path)

    return images
