FROM python:3.9-slim

COPY . /app
WORKDIR /app

RUN apt update -y && apt-get install -y libpq5 libpq-dev
RUN apt install -y python3-pip
RUN python3 -m pip install -r requirements.txt
RUN python3 manage.py migrate
