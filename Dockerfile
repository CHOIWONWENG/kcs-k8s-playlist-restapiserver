# Use the official Python image as the base image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install required packages using pip
RUN pip install -r requirements.txt

# Copy the application code into the container
COPY app app

# Expose the port that the FastAPI app will run on
EXPOSE 8102

# Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8102"]