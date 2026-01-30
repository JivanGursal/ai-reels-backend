from app.services.groq_service import generate_script
from app.services.elevenlabs_service import generate_voice
from app.services.replicate_image import generate_images
from app.services.video_service import generate_video
from app.utils.job_manager import update_job
from app.core.config import settings
from app.utils.files import ensure_dirs

def run_reel_job(job_path, topic, language, mode, seconds):
    ensure_dirs(
        settings.AUDIO_DIR,
        settings.VISUAL_DIR,
        settings.VIDEO_DIR
    )

    try:
        update_job(job_path, status="processing", step="script", progress=10)

        script = generate_script(topic, seconds, language)
        scenes = [s.strip() for s in script.split("\n") if s.strip()]

        update_job(job_path, step="visuals", progress=40)
        visuals = generate_images(scenes)

        update_job(job_path, step="voice", progress=60)
        audio = generate_voice(script, language)

        update_job(job_path, step="rendering", progress=90)
        video = generate_video(visuals, audio, settings.VIDEO_DIR, seconds)

        update_job(
            job_path,
            status="completed",
            progress=100,
            result={"video": video}
        )

    except Exception as e:
        update_job(job_path, status="failed", error=str(e))
