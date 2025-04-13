# Use the official Python base image
FROM python:3-alpine

# Set the working directory
WORKDIR /usr/src/app

# Copy the application code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app will run on
# EXPOSE 8000