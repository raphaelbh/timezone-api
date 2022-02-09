# Timezone API

Timezone API is a simple web service that provides useful time zone services to external third parties.

This project was created with the purpose of deepening knowledge in python, openapi specification, github actions and heroku integration.

**Project status:** in development

## Demo

https://timezone-api-01.herokuapp.com/api/v1/swagger

## Requirements

 - [docker](https://www.docker.com/)
 - [docker compose](https://docs.docker.com/compose/)

## Installation

```bash
$ docker-compose up -d
or
$ docker run -p 5000:5000 -e PORT=5000 -d raphaelbh/timezone-api
```
    
## Usage

```bash
$ curl http://localhost:5000/api/v1/now
$ curl http://localhost:5000/api/v1/timezones
```

## Running Tests

```bash
$ export PYTHONPATH=app
$ pytest --cov-fail-under=90 --cov=app tests/
```

## Tech Stack

- [python](https://www.python.org/)
- [flask](https://flask.palletsprojects.com/en/2.0.x/)
- [open api](https://swagger.io/specification/)
- [docker](https://www.docker.com/)
- [docker compose](https://docs.docker.com/compose/)
- [github actions](https://docs.github.com/en/actions)
- [heroku](https://www.heroku.com/)

## Reference

- https://devcenter.heroku.com/articles/container-registry-and-runtime

## Feedback

If you have any feedback, please contact me at raphaeldias.ti@gmail.com