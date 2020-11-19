# Containerised Web API

Application is developed in python language using flask web framework

/info endpoint which returns a 200 response in JSON format with the following output:

- service_name
- version
- git_commit_sha
- environment

- sample JSON response

```
  {
  "service_name": "myapplication",
  "version": "1.0.0",
  "git_commit_sha": "19a2195fa2470e2780f489620e39ee3f44dce526",
  "environment": {
  "log_level": "INFO",
  "service_port": "8080"
  },
  }
```

## Getting started

Install [git](https://git-scm.com/downloads) and clone my repo [MyApp](https://github.com/kaviit/MyApplication.git)

Install [docker](https://docs.docker.com/engine/installation/)

To build the docker image

```shell
docker build -t myapi:latest .
```

Install [docker-compose](https://docs.docker.com/compose/install/)

To Run the docker in a container

```shell
docker-compose up -d
```

## Tests

- To get the /info endpoint output

```shell
http://localhost:8080/info

or

# curl -s http://localhost:8080/info
```

To stop the container

```shell
docker-compose stop
```

This has been tested on windows(Docker desktop), Amazon Linux 2 AMI, Ubuntu server
