import json
import os
import uuid
from datetime import datetime

def create_job(job_path: str):
    # ✅ ensure jobs directory exists
    os.makedirs(os.path.dirname(job_path), exist_ok=True)

    job_id = os.path.splitext(os.path.basename(job_path))[0]

    data = {
        "id": job_id,
        "status": "queued",
        "created_at": datetime.utcnow().isoformat(),
        "progress": 0,
        "error": None,
        "result": None
    }

    _save(job_path, data)
    return data


def read_job(job_path: str):
    if not os.path.exists(job_path):
        return None
    with open(job_path, "r") as f:
        return json.load(f)


def update_job(job_path: str, **updates):
    job = read_job(job_path)
    if not job:
        return
    job.update(updates)
    _save(job_path, job)


def _save(path: str, data: dict):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
