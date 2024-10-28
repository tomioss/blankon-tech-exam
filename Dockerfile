FROM python:3.10-slim

WORKDIR /usr/src/app
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

