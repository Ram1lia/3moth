FROM python:3.10

EXPOSE 1993

RUN mkdir /opt/services/bot
WORKDIR /opt/services/bot

COPY . /opt/services/bot

RUN pip instaall -r reqirements.txt

CMD ['python','/opt/services/bot/main.py']

