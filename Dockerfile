# syntax=docker/dockerfile:1
# docker build -t knex666/shortipy:latest .
FROM python:3.11.0-slim-buster
WORKDIR /source
ENV FLASK_APP=shorti.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=4321
COPY ./ /source
RUN apt-get update && apt-get install build-essential python3-dev -y
RUN pip3 install -r /source/requirements.txt
CMD ["uwsgi", "app.ini"]
