# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN apt-get update && apt-get install -y curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry && \
    apt-get remove -y curl && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Copy only the necessary files for Poetry installation
COPY pyproject.toml poetry.lock /app/

# Install dependencies using Poetry
RUN poetry config virtualenvs.create false && poetry install --no-root --no-dev

# Copy the application files into the container
COPY . /app

# Expose a port if your app runs on a specific port (e.g., 8000)
EXPOSE 8000

# Command to run your application
CMD ["python", "run.py"]
