# Base image
FROM python:3.9

# Set working directory
WORKDIR watch_next

# Copy requirements.txt file to container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy watch_next files to container
COPY . .

# Expose port 8080
EXPOSE 8080

# Run the watch_next when the container starts
CMD ["python", "watch_next.py"]
