FROM python:3.7

RUN touch /opt/input.txt
RUN touch /opt/output.txt
RUN touch /opt/completed-client-tasks.json
RUN touch /opt/new-client-tasks.json

COPY ./run.sh /run.sh
COPY ./runMaster.sh /runMaster.sh
COPY ./runStation.sh /runStation.sh
COPY ./src /app

WORKDIR /app
RUN pip install -r requirements.txt

WORKDIR /
CMD ["sh", "/run.sh"]