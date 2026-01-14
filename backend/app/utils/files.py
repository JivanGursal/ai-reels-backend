import os

def ensure_dirs(*dirs):
    for d in dirs:
        os.makedirs(d, exist_ok=True)

def unique_filename(prefix, ext):
    import uuid
    return f"{prefix}_{uuid.uuid4().hex}.{ext}"
