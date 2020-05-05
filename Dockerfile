#python basic image
FROM python:3.7-alpine
MAINTAINER Matthew Tozzi

# recommended in docker
ENV PYTHONUNBUFFERED 1
#copy requirements into docker env
COPY ./requirements.txt /requirements.txt
#install requirements
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# seperate user just for app not root
RUN adduser -D user
USER user
