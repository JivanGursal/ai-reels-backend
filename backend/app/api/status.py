from fastapi import APIRouter, HTTPException
from app.core.config import settings
from app.utils.job_manager import read_job
import os

router = APIRouter()

@router.get("/status/{job_id}")
def job_status(job_id: str):
    job_path = os.path.join(settings.JOBS_DIR, job_id)

    job = read_job(job_path)
    if not job:
        raise HTTPException(404, "Job not found")

    return job
