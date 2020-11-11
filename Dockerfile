<<<<<<< HEAD
FROM python:3.8-alpine
RUN apk update && \
    apk upgrade && \
    apk add git

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "myapi.py"]
=======
FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "myapi.py"]
>>>>>>> 70c0f643f2d82a4ebf3e2770c8f81bddeda1836e
