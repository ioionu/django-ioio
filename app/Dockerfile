# Use the official Python image from the Docker Hub
FROM python:3.8.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV HOME=/home/app
ENV APP_HOME=/home/app/web

RUN apt-get update && apt-get install apt-utils python3-psycopg2 -y

# install dependencies
# Copy the requirements.txt file.
# COPY ./Pipfile .
# COPY ./Pipfile.lock .
COPY ./entrypoint.sh .
COPY ./requirements.txt .

# Upgrade pip
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Install deps for entrypont and psycopg.
RUN apt update \
    && apt install libpq-dev gcc netcat -y

# RUN flake8 --ignore=E501,F401 --exclude="node_modules" .

RUN mkdir -p ${APP_HOME}
RUN mkdir ${APP_HOME}/static
RUN mkdir ${APP_HOME}/media
WORKDIR ${APP_HOME}

RUN addgroup --system app
RUN GID=`grep "app" /etc/group|cut -d: -f3` && adduser --system app -gid ${GID}

COPY ./entrypoint.sh ${APP_HOME}

# Copy project.
# COPY --chown=app:app . ${APP_HOME}
# RUN chown -R app:app ${APP_HOME}
USER app

ENTRYPOINT ["/home/app/web/entrypoint.sh"]