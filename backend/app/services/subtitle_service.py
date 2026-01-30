import os
from app.utils.files import unique_filename


def generate_subtitles(script: str, seconds: int, output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)

    lines = [l.strip() for l in script.split("\n") if l.strip()]
    duration = seconds / max(1, len(lines))

    srt = ""
    t = 0.0

    for i, line in enumerate(lines, 1):
        start = _ts(t)
        end = _ts(t + duration)
        srt += f"{i}\n{start} --> {end}\n{line}\n\n"
        t += duration

    filename = unique_filename("subtitles", "srt")
    path = os.path.join(output_dir, filename)

    with open(path, "w", encoding="utf-8") as f:
        f.write(srt)

    return path


def _ts(sec):
    h = int(sec // 3600)
    m = int((sec % 3600) // 60)
    s = int(sec % 60)
    ms = int((sec - int(sec)) * 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"
