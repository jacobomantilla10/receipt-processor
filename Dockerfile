FROM python:3.9-alpine

RUN apk update

WORKDIR /usr/src/app
COPY requirements.txt bootstrap.sh ./
COPY processor ./processor

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["/usr/src/app/bootstrap.sh"]