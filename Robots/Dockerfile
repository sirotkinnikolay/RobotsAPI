FROM python:3.8.6-alpine

WORKDIR /usr/src/app
RUN pip install --upgrade pip

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .