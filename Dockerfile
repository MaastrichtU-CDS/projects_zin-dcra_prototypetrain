FROM python:3.7

RUN touch /opt/input.txt
RUN touch /opt/output.txt
RUN touch /opt/completed-client-tasks.json
RUN touch /opt/new-client-tasks.json
RUN touch /opt/error.log
RUN touch /opt/train.log

COPY ./run.sh /run.sh
COPY ./runMaster.sh /runMaster.sh
COPY ./runStation.sh /runStation.sh
COPY ./src /app

WORKDIR /app
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y dos2unix
RUN dos2unix /run.sh
RUN dos2unix /runMaster.sh
RUN dos2unix /runStation.sh
RUN dos2unix /app/**

WORKDIR /
CMD ["sh", "/run.sh"]