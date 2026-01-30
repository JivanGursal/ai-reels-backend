from fastapi import APIRouter, HTTPException
from app.utils.job_manager import read_job
from app.core.config import settings
import os

router = APIRouter()

@router.get("/status/{job_id}")
def status(job_id: str):
    path = os.path.join(settings.JOBS_DIR, f"{job_id}.json")
    job = read_job(path)
    if not job:
        raise HTTPException(404, "Job not found")
    return job
