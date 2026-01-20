from fastapi import APIRouter, BackgroundTasks
from app.core.config import settings
from app.utils.job_manager import create_job
from app.workers.reel_worker import run_reel_job
from app.utils.files import ensure_dirs
import os

router = APIRouter()

@router.post("/generate")
def generate_reel(
    idea: str,
    seconds: int = 10,
    background_tasks: BackgroundTasks = None
):
    # ✅ 0️⃣ Ensure jobs directory exists
    ensure_dirs(settings.JOBS_DIR)

    # 1️⃣ Create job path FIRST
    job_id = os.urandom(16).hex()
    job_path = os.path.join(settings.JOBS_DIR, f"{job_id}.json")

    # 2️⃣ Create job file
    job = create_job(job_path)

    # 3️⃣ Run worker
    background_tasks.add_task(
        run_reel_job,
        job_path,
        idea,
        seconds
    )

    return {
        "status": "accepted",
        "job_id": job_id
    }
