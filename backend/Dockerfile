FROM python:3.10-slim

WORKDIR /app

# ----------------------------
# System dependencies (CRITICAL)
# ----------------------------
RUN apt-get update && apt-get install -y \
    ffmpeg \
    imagemagick \
    libgl1 \
    espeak-ng \
    build-essential \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# ----------------------------
# Fix ImageMagick policy (VERY IMPORTANT)
# ----------------------------
RUN sed -i 's/rights="none" pattern="PDF"/rights="read|write" pattern="PDF"/' /etc/ImageMagick-6/policy.xml || true \
 && sed -i 's/rights="none" pattern="PNG"/rights="read|write" pattern="PNG"/' /etc/ImageMagick-6/policy.xml || true

# ----------------------------
# Python dependencies
# ----------------------------
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --use-pep517 -r requirements.txt

# ----------------------------
# App
# ----------------------------
COPY . .

EXPOSE 8000

# ----------------------------
# Production-safe Uvicorn
# ----------------------------
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
