FROM python:3.7.4

LABEL maintainer="flavien@berwick.fr"

RUN mkdir /app
WORKDIR /app

COPY ./requirements.txt /
RUN pip install -r /requirements.txt

COPY ./entrypoint.sh /entrypoint.sh

ENV PYTHONPATH "/src"

EXPOSE 8080

ENTRYPOINT [ "bash", "/entrypoint.sh" ]
