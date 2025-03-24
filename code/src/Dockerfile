FROM python:3.9-slim

WORKDIR /app

# Copy the project files
COPY . .

# Install dependencies
RUN pip install -r requirements.txt

# Expose the FastAPI port
EXPOSE 8000

# Run the service
CMD ["python", "main.py"]