FROM python:3.7.3

ENV BASE_DIR /opt/merantix
VOLUME ["$BASE_DIR"]
WORKDIR $BASE_DIR

RUN apt update && apt upgrade -y

COPY requirements.txt $BASE_DIR/requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["pytest"]

