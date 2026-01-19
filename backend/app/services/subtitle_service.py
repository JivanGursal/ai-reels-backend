import os
import srt
from datetime import timedelta
from app.utils.files import unique_filename
from app.core.logger import get_logger
from pathlib import Path

logger = get_logger()


def generate_subtitles(text: str, seconds: int, output_dir: str) -> str:
    """
    STEP-3 FINAL
    Generates word-by-word subtitles (.srt)

    - Simple & fast
    - Works reliably on Render free tier
    - Future me sentence-based subtitles me upgrade possible
    """

    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        words = text.split()
        if not words:
            raise ValueError("Empty text received for subtitles")

        per_word_duration = seconds / len(words)

        subtitles = []
        start_time = 0.0

        for i, word in enumerate(words, start=1):
            subtitles.append(
                srt.Subtitle(
                    index=i,
                    start=timedelta(seconds=start_time),
                    end=timedelta(seconds=start_time + per_word_duration),
                    content=word
                )
            )
            start_time += per_word_duration

        filename = unique_filename("subs", "srt")
        path = os.path.join(output_dir, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(srt.compose(subtitles))

        logger.info(f"Subtitles generated: {path}")
        return path

    except Exception as e:
        logger.exception("Subtitle generation failed")
        raise RuntimeError(f"Subtitle generation error: {str(e)}")
