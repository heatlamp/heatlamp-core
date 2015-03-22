FROM python:2.7.9-slim
MAINTAINER Ash Wilson <smashwilson@gmail.com>

RUN apt-get update
RUN apt-get install -y git
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt
ADD . /usr/src/app

EXPOSE 10100

ENTRYPOINT ["/usr/local/bin/python", "app.py"]
