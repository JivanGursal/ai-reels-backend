# app/utils/job_manager.py

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
        "created_at": datetime.utcnow().isoformat()
    }
    _save(job_path, data)

def update_job(job_path, **kwargs):
    data = _load(job_path)
    data.update(kwargs)
    _save(job_path, data)

def read_job(job_path):
    if not os.path.exists(job_path):
        return None
    return _load(job_path)

def _save(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def _load(path):
    with open(path) as f:
        return json.load(f)
