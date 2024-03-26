FROM python:3.12-alpine

# Use the official lightweight Python image based on Alpine Linux

# Install system dependencies
RUN apk update \
    && apk add --no-cache postgresql-dev gcc musl-dev

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Set working directory
WORKDIR /app

# Copy the application code
COPY . .

# Create a non-root user and give ownership to the app directory
RUN adduser -D appuser -u 5678
RUN chown -R appuser /app

# Switch to the non-root user
USER appuser


