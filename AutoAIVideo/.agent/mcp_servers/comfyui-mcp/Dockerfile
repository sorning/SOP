FROM python:3.11-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy the server script
COPY server.py .

# Run the server on startup
ENTRYPOINT ["python", "server.py"]
