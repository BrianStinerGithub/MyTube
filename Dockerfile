# syntax=docker/dockerfile:1
FROM python:3.9.12
COPY requirements.txt .
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "core/manage.py", "runserver", "8000"]


# docker run --name repo alpine/git clone \
# https://github.com/docker/getting-started.git

# docker cp repo:/git/getting-started/
# cd getting-started

# docker build -t docker101tutorial .


# apk update && apk upgrade && apk add python3

# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1