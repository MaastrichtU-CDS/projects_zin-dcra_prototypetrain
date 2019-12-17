FROM alpine:latest

RUN touch /input.txt
RUN touch /output.txt

COPY ./run.sh /run.sh

CMD ["sh", "/run.sh"]