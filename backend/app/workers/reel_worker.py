import os
from app.services.script_service import generate_script
from app.services.visual_service import generate_visuals
from app.services.voice_service import generate_voice
from app.services.subtitle_service import generate_subtitles
from app.services.video_service import generate_video
from app.core.config import settings
from app.utils.files import ensure_dirs, unique_filename


async def process_reel(job_id: str, idea: str, seconds: int):
    """
    BACKGROUND WORKER
    ⚠️ Ye function HTTP request ke bahar chalta hai
    """

    ensure_dirs(
        settings.AUDIO_DIR,
        settings.VISUAL_DIR,
        settings.SUBTITLE_DIR,
        settings.VIDEO_DIR
    )

    # 1️⃣ Script
    script = generate_script(idea, seconds)

    # 2️⃣ Visuals
    visuals = generate_visuals(
        script,
        max(1, seconds // 3),
        settings.VISUAL_DIR
    )

    # 3️⃣ Voice
    audio_path = await generate_voice(script, settings.AUDIO_DIR)

    # 4️⃣ Subtitles
    subtitles = generate_subtitles(
        script,
        seconds,
        settings.SUBTITLE_DIR
    )

    # 5️⃣ Final video
    video_name = unique_filename("final", "mp4")
    video_path = os.path.join(settings.VIDEO_DIR, video_name)

    generate_video(
        visuals,
        audio_path,
        video_path,
        seconds
    )

    # NOTE:
    # Abhi hum file me status save nahi kar rahe
    # Wo STEP 2 me aayega
