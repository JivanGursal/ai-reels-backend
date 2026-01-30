from fastapi import FastAPI
from app.api.generate import router as generate_router
from app.api.status import router as status_router
from app.core.config import settings
from app.core.logger import get_logger

logger = get_logger()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(generate_router, prefix="/api")
app.include_router(status_router, prefix="/api")

@app.get("/")
def health():
    return {
        "status": "ok",
        "app": settings.APP_NAME,
        "version": settings.VERSION
    }
