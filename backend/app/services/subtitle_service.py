import os
from pathlib import Path
from app.utils.files import unique_filename

def generate_subtitles(script: str, seconds: int, output_dir: str):
    """
    Generates simple SRT subtitles
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    lines = [l.strip() for l in script.split("\n") if l.strip()]
    duration = seconds / max(len(lines), 1)

    filename = unique_filename("subs", "srt")
    path = os.path.join(output_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        current = 0.0
        for i, line in enumerate(lines, start=1):
            start = current
            end = start + duration
            f.write(f"{i}\n")
            f.write(
                f"00:00:{start:05.2f} --> 00:00:{end:05.2f}\n"
            )
            f.write(f"{line}\n\n")
            current = end

    return path
