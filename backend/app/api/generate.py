from fastapi import APIRouter, BackgroundTasks, HTTPException
from pydantic import BaseModel
from app.core.config import settings
from app.utils.job_manager import create_job
from app.workers.reel_worker import run_reel_job
from app.utils.files import ensure_dirs
import os

router = APIRouter()

ALLOWED_LANGUAGES = [
    "english",
    "hindi",
    "marathi",
    "gujarati",
    "kannada",
    "tamil",
    "rajasthani",
]

ALLOWED_MODES = ["script_to_video", "image_to_video"]


class GenerateRequest(BaseModel):
    topic: str
    language: str
    mode: str
    seconds: int = 10


@router.post("/generate")
def generate_reel(
    payload: GenerateRequest,
    background_tasks: BackgroundTasks
):
    # 🔒 Validation
    if payload.language not in ALLOWED_LANGUAGES:
        raise HTTPException(status_code=400, detail="Unsupported language")

    if payload.mode not in ALLOWED_MODES:
        raise HTTPException(status_code=400, detail="Unsupported mode")

    if payload.seconds <= 0 or payload.seconds > 60:
        raise HTTPException(status_code=400, detail="Invalid duration")

    ensure_dirs(settings.JOBS_DIR)

    job_id = os.urandom(16).hex()
    job_path = os.path.join(settings.JOBS_DIR, f"{job_id}.json")

    create_job(job_path)

    background_tasks.add_task(
        run_reel_job,
        job_path,
        payload.topic,
        payload.language,
        payload.mode,
        payload.seconds
    )

    return {
        "status": "accepted",
        "job_id": job_id
    }
