FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH="$PYTHONPATH:/project"
ENV FLASK_APP=user_facing_api.py
ENV FLASK_ENV=development
ENV FLASK_DEBUG=1

ARG POETRY_VERSION=1.0.5
ARG POETRY_VIRTUALENVS_CREATE=false

RUN mkdir /project
WORKDIR /project
COPY . /project/

RUN pip install "poetry==$POETRY_VERSION"
RUN poetry install