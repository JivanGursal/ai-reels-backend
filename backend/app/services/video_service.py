import os
from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
from app.utils.files import unique_filename
from app.core.logger import get_logger
from pathlib import Path

logger = get_logger()


def generate_video(
    images: list[str],
    audio_path: str,
    output_dir: str,
    seconds: int,
    fps: int = 24
) -> str:
    """
    STEP-3 FINAL VIDEO RENDERER

    - Render-safe
    - Low RAM friendly
    - Deterministic output
    """

    if not images:
        raise ValueError("No images provided for video generation")

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    Path(output_dir).mkdir(parents=True, exist_ok=True)

    clips = []

    try:
        audio = AudioFileClip(audio_path)

        duration_per_image = audio.duration / len(images)

        for img in images:
            clip = (
                ImageClip(img)
                .set_duration(duration_per_image)
            )
            clips.append(clip)

        video = concatenate_videoclips(clips, method="compose")
        video = video.set_audio(audio)

        filename = unique_filename("final", "mp4")
        output_path = os.path.join(output_dir, filename)

        video.write_videofile(
            output_path,
            fps=fps,
            codec="libx264",
            audio_codec="aac",
            threads=2,          # 🔥 Render free-tier safe
            preset="medium",
            verbose=False,
            logger=None
        )

        logger.info(f"Video rendered successfully: {output_path}")
        return output_path

    except Exception as e:
        logger.exception("Video rendering failed")
        raise RuntimeError(f"Video rendering error: {str(e)}")

    finally:
        # 🔥 VERY IMPORTANT CLEANUP
        try:
            for clip in clips:
                clip.close()
            if 'audio' in locals():
                audio.close()
            if 'video' in locals():
                video.close()
        except Exception:
            pass
