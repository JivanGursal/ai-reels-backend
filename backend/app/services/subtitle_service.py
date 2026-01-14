import srt
from datetime import timedelta
from app.utils.files import unique_filename
import os

def generate_subtitles(text: str, seconds: int, output_dir: str):
    words = text.split()
    per_word = seconds / max(len(words), 1)

    subtitles = []
    start = 0.0

    for i, word in enumerate(words):
        subtitles.append(
            srt.Subtitle(
                index=i,
                start=timedelta(seconds=start),
                end=timedelta(seconds=start + per_word),
                content=word
            )
        )
        start += per_word

    filename = unique_filename("subs", "srt")
    path = os.path.join(output_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(srt.compose(subtitles))

    return path
