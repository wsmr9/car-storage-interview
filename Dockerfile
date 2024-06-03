# Use an official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container to /app
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application source code from the current directory to /app in the container
COPY . .

# Set environment variables from arguments passed at build-time
ARG DATABASE_URL
ENV DATABASE_URL=${DATABASE_URL}

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py
ENV FLASK_ENV=development

# Run the application when the container launches
CMD ["python", "run.py"]
