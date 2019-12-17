FROM alpine:latest

RUN touch /input.txt
RUN touch /output.txt

COPY ./run.sh /run.sh
COPY ./runMaster.sh /runMaster.sh
COPY ./runStation.sh /runStation.sh

CMD ["sh", "/run.sh"]