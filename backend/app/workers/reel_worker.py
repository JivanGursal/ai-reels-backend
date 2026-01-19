from app.services.script_service import generate_script
from app.services.visual_service import generate_visuals
from app.services.voice_service import generate_voice_sync
from app.services.subtitle_service import generate_subtitles
from app.services.video_service import generate_video
from app.core.config import settings
from app.utils.files import ensure_dirs
from app.utils.job_manager import update_job


def run_reel_job(job_path: str, idea: str, seconds: int):
    """
    BACKGROUND WORKER (SYNC)
    ✔ Render compatible
    ✔ Beginner friendly
    ✔ Job progress enabled
    """

    ensure_dirs(
        settings.AUDIO_DIR,
        settings.VISUAL_DIR,
        settings.SUBTITLE_DIR,
        settings.VIDEO_DIR
    )

    try:
        # 1️⃣ Script
        update_job(job_path, status="processing", step="generating_script", progress=10)
        script = generate_script(idea, seconds)

        # 2️⃣ Visuals
        update_job(job_path, step="generating_visuals", progress=30)
        visuals = generate_visuals(
            script,
            max(1, seconds // 3),
            settings.VISUAL_DIR
        )

        # 3️⃣ Voice
        update_job(job_path, step="generating_voice", progress=50)
        audio_path = generate_voice_sync(script, settings.AUDIO_DIR)

        # 4️⃣ Subtitles
        update_job(job_path, step="generating_subtitles", progress=70)
        subtitles = generate_subtitles(script, seconds, settings.SUBTITLE_DIR)

        # 5️⃣ Final Video
        update_job(job_path, step="rendering_video", progress=90)
        video_path = generate_video(
            visuals,
            audio_path,
            settings.VIDEO_DIR
        )

        update_job(
            job_path,
            status="completed",
            step="done",
            progress=100,
            video=video_path,
            subtitles=subtitles
        )

    except Exception as e:
        update_job(
            job_path,
            status="failed",
            step="error",
            error=str(e)
        )
