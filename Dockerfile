FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNUNBUFFERED 1

WORKDIR /usr/src/dm_rest

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
RUN pip install psycopg2-binary

COPY . /usr/src/dm_rest