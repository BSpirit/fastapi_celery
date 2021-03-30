# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /api
WORKDIR /api

# Copy the current directory contents into the container at /api
COPY . /api

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose port 8000
EXPOSE 8000
