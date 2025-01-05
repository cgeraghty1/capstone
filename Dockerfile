# Use the official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the local project files to the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir dash plotly pandas

# Expose the port that the app will run on
EXPOSE 8080

# Start the application
CMD ["python", "fisher_statistical_app.py"]



