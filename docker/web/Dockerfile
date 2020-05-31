# pull official base image
FROM python:3.8.1-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV APP_ROOT /usr/src/app

# set work directory
RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

# copy project
RUN mkdir ${APP_ROOT}/app
COPY ./app ${APP_ROOT}/app
COPY manage.py ${APP_ROOT}
COPY requirements.txt ${APP_ROOT}


# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 5000