import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "AI Reels Generator"
    VERSION = "1.0.0"

    OUTPUT_DIR = "backend/output"
    AUDIO_DIR = f"{OUTPUT_DIR}/audio"
    VISUAL_DIR = f"{OUTPUT_DIR}/visuals"
    SUBTITLE_DIR = f"{OUTPUT_DIR}/subtitles"
    VIDEO_DIR = f"{OUTPUT_DIR}/videos"

    # Visual AI (FREE / local first)
    SD_API_URL = os.getenv("SD_API_URL", "")  # optional future use

settings = Settings()
