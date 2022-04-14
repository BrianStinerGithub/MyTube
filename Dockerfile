# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/


# docker run --name repo alpine/git clone \
# https://github.com/docker/getting-started.git

# docker cp repo:/git/getting-started/
# cd getting-started

# docker build -t docker101tutorial .


# apk update && apk upgrade && apk add python3

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1