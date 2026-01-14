from fastapi import APIRouter
from app.services.script_service import generate_script
from app.services.visual_service import generate_visuals
from app.services.voice_service import generate_voice
from app.services.subtitle_service import generate_subtitles
from app.services.video_service import generate_video
from app.core.config import settings
from app.utils.files import ensure_dirs, unique_filename
import asyncio
import os

router = APIRouter()

@router.post("/generate")
async def generate_reel(idea: str, seconds: int = 10):
    ensure_dirs(
        settings.AUDIO_DIR,
        settings.VISUAL_DIR,
        settings.SUBTITLE_DIR,
        settings.VIDEO_DIR
    )

    script = generate_script(idea, seconds)

    visuals = generate_visuals(script, max(1, seconds // 3), settings.VISUAL_DIR)

    audio_path = await generate_voice(script, settings.AUDIO_DIR)

    subtitles = generate_subtitles(script, seconds, settings.SUBTITLE_DIR)

    video_name = unique_filename("final", "mp4")
    video_path = os.path.join(settings.VIDEO_DIR, video_name)

    generate_video(visuals, audio_path, video_path, seconds)

    return {
        "status": "success",
        "video": video_path,
        "subtitles": subtitles
    }
