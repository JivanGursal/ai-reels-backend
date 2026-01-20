from fastapi import APIRouter, BackgroundTasks
from app.core.config import settings
from app.utils.job_manager import create_job
from app.workers.reel_worker import run_reel_job
import os
import uuid

router = APIRouter()

@router.post("/generate")
def generate_reel(
    idea: str,
    seconds: int = 10,
    background_tasks: BackgroundTasks = BackgroundTasks()
):
    # 1️⃣ Generate job_id & job_path
    job_id = str(uuid.uuid4())
    job_path = os.path.join(settings.JOBS_DIR, f"{job_id}.json")

    # 2️⃣ Create job file
    job = create_job(job_path)

    # 3️⃣ Run worker in background
    background_tasks.add_task(
        run_reel_job,
        job_path,
        idea,
        seconds
    )

    # 4️⃣ Immediate response
    return {
        "status": "accepted",
        "job_id": job_id
    }
