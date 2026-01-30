from app.services.script_service import generate_script
from app.services.replicate_image import generate_images
from app.services.elevenlabs_service import generate_voice
from app.services.subtitle_service import generate_subtitles
from app.services.video_service import generate_video
from app.core.config import settings
from app.utils.files import ensure_dirs
from app.utils.job_manager import update_job


def run_reel_job(
    job_path: str,
    topic: str,
    language: str,
    mode: str,
    seconds: int
):
    """
    OPTION A — FINAL BACKGROUND WORKER
    ✔ Render safe
    ✔ Memory friendly
    ✔ Language aware
    """

    ensure_dirs(
        settings.AUDIO_DIR,
        settings.VISUAL_DIR,
        settings.SUBTITLE_DIR,
        settings.VIDEO_DIR,
    )

    try:
        update_job(job_path, status="processing", step="script", progress=10)

        # 🧠 1. Script (Groq)
        script = generate_script(
            topic=topic,
            language=language,
            seconds=seconds
        )

        # 🖼️ 2. Images (Replicate SD)
        update_job(job_path, step="visuals", progress=30)
        images = generate_images(
            script=script,
            count=max(1, seconds // 3),
            output_dir=settings.VISUAL_DIR
        )

        # 🔊 3. Voice (ElevenLabs)
        update_job(job_path, step="voice", progress=55)
        audio_path = generate_voice(
            text=script,
            language=language,
            output_dir=settings.AUDIO_DIR
        )

        # 📝 4. Subtitles
        update_job(job_path, step="subtitles", progress=70)
        subtitles = generate_subtitles(
            script=script,
            seconds=seconds,
            output_dir=settings.SUBTITLE_DIR
        )

        # 🎬 5. Video render
        update_job(job_path, step="video", progress=90)
        video_path = generate_video(
            images=images,
            audio_path=audio_path,
            output_dir=settings.VIDEO_DIR,
            seconds=seconds
        )

        update_job(
            job_path,
            status="completed",
            step="done",
            progress=100,
            result={
                "video": video_path,
                "subtitles": subtitles
            }
        )

    except Exception as e:
        update_job(
            job_path,
            status="failed",
            step="error",
            error=str(e)
        )
