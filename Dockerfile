# Use stable Python version
FROM python:3.11.9

# Set work directory in container
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Flask's default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
