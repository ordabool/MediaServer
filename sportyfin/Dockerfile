FROM python:3.8-slim-buster

WORKDIR /sportyfin

COPY ./requirements.txt /sportyfin/
RUN pip install -r requirements.txt

CMD [ "python3", "-m" , "sportyfin", "run", "-ef", "-o", "/sportyfin/output" ]
