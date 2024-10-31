# Use an official Ubuntu as a base image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install necessary packages
RUN apt-get update && apt-get install -y python3 python3-pip

# Run the Python script by default
CMD ["bash", "-c", "python3 /app/projectone.py && tail -f /dev/null"]


