from fastapi import APIRouter, BackgroundTasks
from app.utils.job_manager import create_job
from app.workers.reel_worker import run_reel_job
from app.core.config import settings
import os, uuid

router = APIRouter()

@router.post("/generate")
def generate(
    topic: str,
    language: str,
    mode: str,
    seconds: int,
    bg: BackgroundTasks
):
    job_id = uuid.uuid4().hex
    job_path = os.path.join(settings.JOBS_DIR, f"{job_id}.json")

    create_job(job_path)

    bg.add_task(
        run_reel_job,
        job_path,
        topic,
        language,
        mode,
        seconds
    )

    return {"job_id": job_id}
