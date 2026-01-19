import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "AI Reels Generator"
    VERSION = "1.0.0"

    # ✅ ONE ROOT STORAGE
    STORAGE_DIR = "storage"

    AUDIO_DIR = f"{STORAGE_DIR}/audio"
    VISUAL_DIR = f"{STORAGE_DIR}/visuals"
    SUBTITLE_DIR = f"{STORAGE_DIR}/subtitles"
    VIDEO_DIR = f"{STORAGE_DIR}/videos"
    JOBS_DIR = f"{STORAGE_DIR}/jobs"

    # Visual AI (future / optional)
    SD_API_URL = os.getenv("SD_API_URL", "")


settings = Settings()
