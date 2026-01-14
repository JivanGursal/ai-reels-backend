from loguru import logger
import sys

logger.remove()
logger.add(
    sys.stdout,
    format="<green>{time}</green> | <level>{level}</level> | <level>{message}</level>",
    level="INFO"
)

def get_logger():
    return logger
