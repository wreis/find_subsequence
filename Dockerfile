FROM python:3.7.3

ENV BASE_DIR /opt/merantix
VOLUME ["$BASE_DIR"]
WORKDIR $BASE_DIR

RUN apt update && apt upgrade -y

COPY . $BASE_DIR/

RUN pip install --upgrade pip && pip install setuptools
RUN pip install -r requirements.txt

RUN pytest -v tests.py