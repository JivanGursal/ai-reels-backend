import uuid
from pathlib import Path
from TTS.api import TTS
from app.core.logger import get_logger

logger = get_logger()

_tts = None  # Global cached TTS model


def get_tts():
    """
    Loads TTS model only once (VERY IMPORTANT for Render / low RAM servers)
    """
    global _tts
    if _tts is None:
        logger.info("Loading TTS model (first time)...")
        _tts = TTS(
            model_name="tts_models/en/vctk/vits",
            progress_bar=False,
            gpu=False
        )
    return _tts


def generate_voice_sync(text: str, output_dir: str) -> str:
    """
    Generates voice-over audio from text.
    STEP-3 FINAL | Free-tier | Local TTS

    NOTE:
    - Sync function by design
    - Background worker me call hoga
    """

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    try:
        tts = get_tts()

        filename = f"voice_{uuid.uuid4().hex}.wav"
        output_path = str(Path(output_dir) / filename)

        tts.tts_to_file(
            text=text,
            file_path=output_path,
            speaker=tts.speakers[0]
        )

        logger.info(f"Voice generated: {output_path}")
        return output_path

    except Exception as e:
        logger.exception("Voice generation failed")
        raise RuntimeError(f"TTS failed: {str(e)}")
