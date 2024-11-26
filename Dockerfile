# Use a lightweight Python base image
FROM python:3.11-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Expose the port on which the app will run
EXPOSE 8080

# Command to run the app
CMD ["python", "app.py"]
