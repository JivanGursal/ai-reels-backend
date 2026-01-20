from fastapi import APIRouter, BackgroundTasks
from app.core.config import settings
from app.utils.job_manager import create_job
from app.workers.reel_worker import run_reel_job
import os

router = APIRouter()

@router.post("/generate")
def generate_reel(
    idea: str,
    seconds: int = 10,
    background_tasks: BackgroundTasks = None
):
    # 1️⃣ Create Job
    job = create_job()
    job_path = os.path.join(settings.JOBS_DIR, f"{job['id']}.json")

    # 2️⃣ Run worker in background
    background_tasks.add_task(
        run_reel_job,
        job_path,
        idea,
        seconds
    )

    # 3️⃣ Immediate response (NO BLOCKING)
    return {
        "status": "accepted",
        "job_id": job["id"]
    }
