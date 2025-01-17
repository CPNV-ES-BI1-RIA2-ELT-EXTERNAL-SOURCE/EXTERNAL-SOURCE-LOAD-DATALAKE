# Use a basic image
FROM python:3.13-slim

# Install pipenv
RUN pip install pipenv

# Define working directory
WORKDIR /app

# Copy Pipenv files and install dependencies
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

# Copy application files
COPY . .

# Copy environment file
COPY .env /app/.env

# Expose the specified port
ARG SERVER_PORT
EXPOSE ${SERVER_PORT}

# Configuring behavior to suit the environment
CMD ["sh", "-c", "if [ \"$ENVIRONMENT\" = 'production' ]; then uvicorn app:app --host 0.0.0.0 --port ${SERVER_PORT}; else uvicorn app:app --host 0.0.0.0 --port ${SERVER_PORT} --reload; fi"]
