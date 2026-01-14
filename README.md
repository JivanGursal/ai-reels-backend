# AI Reels Generator Backend

## Run locally
uvicorn app.main:app --reload

## API
POST /generate
Params:
- idea
- seconds

## Deploy
Docker + Gunicorn ready
