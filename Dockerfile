FROM python:3.8-alpine
RUN apk update && \
    apk upgrade && \
    apk add git

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["python", "myapi.py"]
