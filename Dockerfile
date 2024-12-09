# Use the official Python image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents to the container
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir dash plotly pandas

# Expose the port that the Dash app runs on
EXPOSE 8080

# Run the application
CMD ["python", "fisher_dash_app.py"]
