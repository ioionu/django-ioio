# Use the official Python image from the Docker Hub
FROM python:3.8.6

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
# Copy the requirements.txt file.
COPY ./Pipfile .
COPY ./Pipfile.lock .

# Upgrade pip
RUN pip install --upgrade pip
RUN pip install --upgrade pipenv
RUN pipenv install --dev --system --deploy

# copy project
COPY . .


