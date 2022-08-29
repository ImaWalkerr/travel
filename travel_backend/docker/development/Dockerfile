FROM python:3.10.4

ENV PYTHONUNBUFFERED=1

ARG CUID=1000

RUN sudo apt-get update && sudo apt-get install -y gss libpq-dev && rm -rf /var/lib/apt/lists/* && sudo apt-get clean

RUN groupadd --gid $CUID django && useradd --uid $CUID --gid django --shell /bin/bash --create-home django

WORKDIR /home/django/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./
