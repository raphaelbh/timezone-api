# Timezone API

[![Project Status](https://img.shields.io/static/v1?label=project%20status&message=complete&color=success&style=flat-square)](#)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/raphaelbh/python-web-template/python-application?style=flat-square)](#)
[![GitHub License](https://img.shields.io/github/license/raphaelbh/python-web-template?style=flat-square)](#)
[![GitHub last commit](https://img.shields.io/github/last-commit/raphaelbh/python-web-template?style=flat-square)](#)

Timezone API is a simple web service that provides useful time zone services to external third parties.

This project was created with the purpose of deepening knowledge in python, openapi specification, github actions and heroku integration.

**Project status:** in development

## Demo

https://timezone-api-01.herokuapp.com/api/v1/swagger

## Requirements

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

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
$ pytest --cache-clear --cov=app tests/
```

## Tech Stack

[![docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.0.x/)
[![swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white)](https://swagger.io/)
[![heroku](https://img.shields.io/badge/Heroku-430098?style=for-the-badge&logo=heroku&logoColor=white)](https://heroku.com)

## Reference

- https://devcenter.heroku.com/articles/container-registry-and-runtime

## Feedback

If you have any feedback, please contact me at raphaeldias.ti@gmail.com

[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/raphaelbh)
[![linkedin](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raphaelbh/)
