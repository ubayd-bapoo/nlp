# Use the official python image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy just the requirements.txt file first and install Python dependencies
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y python3 python3-pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the local script and requirements.txt to the container
COPY . /app/

EXPOSE 8000

HEALTHCHECK --interval=60s --timeout=5s \
    CMD curl -s --fail http://localhost:8000/meta/health

# Run the script when the container starts
CMD ["uvicorn", "service:app", "--host", "0.0.0.0", "--port", "8000"]