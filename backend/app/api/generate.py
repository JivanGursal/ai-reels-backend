# app/api/generate.py

from fastapi import APIRouter, BackgroundTasks
from app.core.config import settings
from app.utils.files import ensure_dirs, unique_filename
from app.utils.job_manager import create_job
from app.worker.reel_worker import run_reel_job
import os

router = APIRouter()

@router.post("/generate")
def generate_reel(
    idea: str,
    seconds: int = 10,
    background_tasks: BackgroundTasks = None
):
    ensure_dirs(settings.JOBS_DIR)

    job_id = unique_filename("job", "json")
    job_path = os.path.join(settings.JOBS_DIR, job_id)

    create_job(job_path)

    background_tasks.add_task(
        run_reel_job,
        job_path,
        idea,
        seconds
    )

    return {
        "job_id": job_id,
        "status": "queued"
    }
