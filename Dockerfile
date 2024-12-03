# Step 1: Use a base image with Python
FROM python:3.12-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the pyproject.toml and poetry.lock to the container
COPY pyproject.toml poetry.lock /app/

# Step 4: Install Poetry and dependencies
RUN pip install --no-cache-dir poetry \
    && poetry install --no-root --no-dev

# Step 5: Copy the rest of the application code into the container
COPY . /app/

# Step 6: Expose the port that Flask will run on (default is 5000)
EXPOSE 5000

# Step 7: Set the command to run the Flask application
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]