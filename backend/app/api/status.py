from fastapi import APIRouter, HTTPException
from app.utils.job_manager import load_job
import os

router = APIRouter()

@router.get("/status/{job_id}")
def get_status(job_id: str):
    job_path = f"backend/app/jobs/{job_id}.json"

    if not os.path.exists(job_path):
        raise HTTPException(status_code=404, detail="Job not found")

    return load_job(job_path)
