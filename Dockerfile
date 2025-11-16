# -----------------------
# Base Image
# -----------------------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# -----------------------
# Install system packages + MySQL client libraries
# -----------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# -----------------------
# Install Python dependencies
# -----------------------
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# -----------------------
# Copy project files
# -----------------------
COPY . .

# -----------------------
# Static files collection (skip error exit on missing directory)
# -----------------------
RUN python manage.py collectstatic --noinput || true

# -----------------------
# Expose the port
# -----------------------
EXPOSE 8000

# -----------------------
# Start with Gunicorn
# -----------------------
CMD ["gunicorn", "StorePilot.wsgi:application", "--bind", "0.0.0.0:8000"]
