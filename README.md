# Containerised Web API

Application is developed in python language using flask web framework

## Getting started

Install [git](https://git-scm.com/downloads) and clone my repo [MyApp](https://github.com/kaviit/MyApplication.git)

Install [docker](https://docs.docker.com/engine/installation/)

To build the docker image

```shell
docker build -t myapi:latest .
```

install [docker-compose](https://docs.docker.com/compose/install/)

To Run the docker in a container

```shell
docker-compose up -d
# docker-compose stop
```

## Tests

- To get the /info endpoint output

```shell

http://localhost:8080/info

# curl -s http://localhost:8080/info
```
