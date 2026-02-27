# Multi-stage Dockerfile for AI Cinematic Universe
FROM python:3.10-slim AS builder

WORKDIR /app

# Install system dependencies for media processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure scripts and outputs are accessible
RUN mkdir -p logs outputs assets

ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["python", "main.py"]
CMD ["--prompt", "A cinematic sunrise over a digital ocean"]
