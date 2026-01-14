from app.core.logger import get_logger
from app.utils.files import unique_filename
import os

logger = get_logger()

def generate_visuals(script: str, scenes: int, output_dir: str):
    visuals = []

    for i in range(scenes):
        filename = unique_filename(f"scene_{i}", "png")
        path = os.path.join(output_dir, filename)

        # TEMP visual placeholder (black frame)
        from PIL import Image
        img = Image.new("RGB", (1080, 1920), color="black")
        img.save(path)

        visuals.append(path)
        logger.info(f"Visual generated: {path}")

    return visuals
