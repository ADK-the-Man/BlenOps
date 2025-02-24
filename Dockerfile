# Use a minimal Blender image as the base
FROM linuxserver/blender:latest AS builder

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-venv ffmpeg fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Create and activate virtual environment
RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Install Python dependencies
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt  

# Copy application files
COPY . .

# Create a lightweight final runtime image
FROM debian:bookworm-slim

# Install only runtime dependencies (not full Blender UI)
RUN apt-get update && apt-get install -y \
    ffmpeg fonts-dejavu libgl1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /usr /usr


# Copy the application and virtual environment
COPY --from=builder /app /app
ENV PATH="/app/venv/bin:$PATH"

# Expose port for Flask
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]