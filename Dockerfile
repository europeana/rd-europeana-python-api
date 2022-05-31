FROM ubuntu:22.04

RUN apt-get update \
    && apt-get install wget -y \
    && apt-get install python3-pip -y \
    && apt install libjpeg-dev zlib1g-dev -y \
    && pip install --upgrade pip 

RUN wget https://github.com/jgm/pandoc/releases/download/2.18/pandoc-2.18-1-amd64.deb \
    && dpkg -i pandoc-2.18-1-amd64.deb
 
WORKDIR /code
COPY . /code/

RUN pip install poetry \
    && poetry install 






