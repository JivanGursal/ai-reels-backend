from fastapi import FastAPI
from app.api.generate import router as generate_router
from app.api.status import router as status_router
from app.core.logger import get_logger

logger = get_logger()

app = FastAPI(
    title="AI Reels Generator",
    version="1.0.0"
)

# 🔹 Routers
app.include_router(generate_router)
app.include_router(status_router)

# 🔹 Health check
@app.get("/")
def health():
    return {"status": "running"}
