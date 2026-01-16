import json
import os
from datetime import datetime

def create_job(job_path):
    data = {
        "status": "queued",
        "step": "waiting",
        "progress": 0,
        "video": None,
        "error": None,
        "updated_at": datetime.utcnow().isoformat()
    }
    save_job(job_path, data)

def update_job(job_path, **kwargs):
    data = load_job(job_path)
    data.update(kwargs)
    data["updated_at"] = datetime.utcnow().isoformat()
    save_job(job_path, data)

def load_job(job_path):
    with open(job_path, "r") as f:
        return json.load(f)

def save_job(job_path, data):
    os.makedirs(os.path.dirname(job_path), exist_ok=True)
    with open(job_path, "w") as f:
        json.dump(data, f, indent=2)
