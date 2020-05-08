#python basic image
FROM python:3.7-alpine
MAINTAINER Matthew Tozzi

# recommended in docker
ENV PYTHONUNBUFFERED 1
#copy requirements into docker env
COPY ./requirements.txt /requirements.txt
#postgres dependency
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
#install requirements
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

# seperate user just for app not root
RUN adduser -D user
USER user
