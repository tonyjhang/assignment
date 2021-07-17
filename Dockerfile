FROM ubuntu:18.04
RUN apt update && apt install -y \
    python3.7 python3.7-dev python3-distutils uwsgi uwsgi-src \
    python3-pip
COPY . /src
WORKDIR /src
RUN python3.7 -m pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT ["/bin/sh", "/src/entrypoint.sh"]