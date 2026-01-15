from fastapi import APIRouter
import asyncio
from app.workers.reel_worker import process_reel
from app.utils.files import unique_filename

router = APIRouter()


@router.post("/generate")
async def generate_reel(idea: str, seconds: int = 10):
    """
    SAFE ENDPOINT
    ✔️ Sirf job start karega
    ✔️ Heavy kaam background me
    """

    job_id = unique_filename("job", "txt")

    # Background task start
    asyncio.create_task(
        process_reel(job_id, idea, seconds)
    )

    return {
        "status": "started",
        "job_id": job_id,
        "message": "Reel generation started in background"
    }
