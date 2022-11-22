FROM python:3.10.8-slim-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /app/requirements.txt

# Install packages
RUN apt-get update && apt-get install -y\
  git gcc libpq-dev \
  && python3 -m pip install -r /app/requirements.txt --no-cache-dir \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . /app/