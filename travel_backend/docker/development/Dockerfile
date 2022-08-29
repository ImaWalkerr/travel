FROM python:3.10.4

ENV PYTHONUNBUFFERED=1

WORKDIR /home/django/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./
