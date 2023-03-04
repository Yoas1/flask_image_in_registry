FROM ubuntu:20.04

WORKDIR /App

COPY . /App


RUN apt-get update -y && \
    apt-get install -y python3 python3-pip curl && \
    pip3 install -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

RUN chmod +x run.sh
ENV FLASK_APP=reg.py
ENV FLASK_DEBUG=1


ENTRYPOINT ["./run.sh"]
