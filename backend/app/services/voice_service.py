import uuid
from pathlib import Path
from TTS.api import TTS

_tts = None  # global cache

def get_tts():
    global _tts
    if _tts is None:
        _tts = TTS(
            model_name="tts_models/en/vctk/vits",
            progress_bar=False,
            gpu=False
        )
    return _tts

async def generate_voice(text: str, output_dir: str) -> str:
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    tts = get_tts()

    filename = f"voice_{uuid.uuid4().hex}.wav"
    output_path = str(Path(output_dir) / filename)

    tts.tts_to_file(
        text=text,
        file_path=output_path,
        speaker=tts.speakers[0]
    )

    return output_path
