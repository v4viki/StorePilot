# -----------------------
# Base Image
# -----------------------
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system packages + MySQL client
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    python3-dev


# Install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Start Gunicorn
CMD ["gunicorn", "StorePilot.wsgi:application", "--bind", "0.0.0.0:8000"]
