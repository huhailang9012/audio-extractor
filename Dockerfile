FROM python:3.8

MAINTAINER Jerry<huhailang@yahoo.cn>

RUN pip install fastapi uvicorn requests -i https://mirrors.aliyun.com/pypi/simple/

RUN echo "deb [check-valid-until=no] http://archive.debian.org/debian jessie-backports main" > /etc/apt/sources.list.d/jessie-backports.list
RUN sed -i '/deb http:\/\/deb.debian.org\/debian jessie-updates main/d' /etc/apt/sources.list
RUN apt-get -o Acquire::Check-Valid-Until=false update
RUN apt-get -y --force-yes install yasm ffmpeg

WORKDIR /code

COPY docker/api /code/
RUN cd /code
CMD uvicorn controller:app --reload --port 8002 --host 0.0.0.0

