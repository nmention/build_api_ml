# Use a lightweight Python image
FROM python:3.11-slim

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn httpx pandas sqlmodel
# Copy the application code
COPY main.py /app/main.py
# Set the working directory to /app
WORKDIR /app
# Expose UDS path as a volume
VOLUME ["/tmp", "./database.db:/app/database.db"]
# Run Uvicorn using the Unix Domain Socket
CMD ["uvicorn", "main:app", "--uds", "/tmp/service_b.sock", "--reload"]
