import os
from PIL import Image
from app.core.logger import get_logger
from app.utils.files import unique_filename

logger = get_logger()

def generate_visuals(script: str, scenes: int, output_dir: str):
    """
    Generates placeholder visuals for each scene.
    (STEP-3 compatible | Free-tier | Render-safe)

    NOTE:
    - Abhi black frames use ho rahe hain
    - STEP-5 me yahi function image/video AI se replace hoga
    """

    os.makedirs(output_dir, exist_ok=True)
    visuals = []

    for i in range(scenes):
        filename = unique_filename(f"scene_{i}", "png")
        path = os.path.join(output_dir, filename)

        # 1080x1920 = Instagram Reels / Shorts standard
        image = Image.new("RGB", (1080, 1920), color=(0, 0, 0))
        image.save(path, format="PNG")

        visuals.append(path)
        logger.info(f"Visual generated: {path}")

    return visuals
