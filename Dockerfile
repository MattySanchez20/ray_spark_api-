# Start from a base OpenJDK image
FROM adoptopenjdk:8-jdk-hotspot

# Install Python 3.10
RUN apt-get update && \
    apt-get install -y python3.10 python3-pip && \
    apt-get clean;

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "main.py"]