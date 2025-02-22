FROM tiangolo/uvicorn-gunicorn:python3.11-slim

LABEL maintainer="Nuttaphat Arunoprayoch"

# Install dependencies
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt


# Copy app to container
COPY ./app /app
WORKDIR /app

# Open port
EXPOSE 80