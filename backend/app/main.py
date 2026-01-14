from fastapi import FastAPI
from app.api.generate import router
from app.core.logger import get_logger

logger = get_logger()

app = FastAPI(
    title="AI Reels Generator",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"status": "running"}
