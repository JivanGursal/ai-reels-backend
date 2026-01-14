from moviepy.editor import ImageClip, AudioFileClip, concatenate_videoclips
import os
import uuid


def generate_video(images, audio_path, output_dir, fps=24):
    if not images:
        raise ValueError("No images provided for video generation")

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    os.makedirs(output_dir, exist_ok=True)

    audio = AudioFileClip(audio_path)
    duration_per_image = audio.duration / len(images)

    clips = []
    for img in images:
        clip = (
            ImageClip(img)
            .set_duration(duration_per_image)
            .set_fps(fps)
        )
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")
    video = video.set_audio(audio)

    output_path = os.path.join(
        output_dir,
        f"final_{uuid.uuid4().hex}.mp4"
    )

    video.write_videofile(
        output_path,
        fps=fps,
        codec="libx264",
        audio_codec="aac",
        threads=4,
        preset="medium",
        verbose=False,
        logger=None
    )

    # 🔥 VERY IMPORTANT CLEANUP
    video.close()
    audio.close()
    for clip in clips:
        clip.close()

    return output_path
