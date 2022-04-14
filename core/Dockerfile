FROM python:3.9.12
EXPOSE 8000 8080
WORKDIR /core
COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir
CMD ["python3", "manage.py", "runserver", "8000"]

# docker run --name repo alpine/git clone \
# https://github.com/docker/getting-started.git

# docker cp repo:/git/getting-started/
# cd getting-started

# docker build -t docker101tutorial .


# apk update && apk upgrade && apk add python3