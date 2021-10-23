FROM python:3.9.7-slim-buster

RUN apt-get update

RUN mkdir /app
ADD . /app/
RUN pip install -r /app/requirements.txt

CMD python /app/main.py /app/config.yml