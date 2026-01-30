import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME = "AI Reels Generator"
    VERSION = "2.0.0"

    BASE_DIR = "storage"

    AUDIO_DIR = f"{BASE_DIR}/audio"
    VISUAL_DIR = f"{BASE_DIR}/visuals"
    VIDEO_DIR = f"{BASE_DIR}/videos"
    SUBTITLE_DIR = f"{BASE_DIR}/subtitles"
    JOBS_DIR = f"{BASE_DIR}/jobs"

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    REPLICATE_API_TOKEN = os.getenv("REPLICATE_API_TOKEN")

settings = Settings()
