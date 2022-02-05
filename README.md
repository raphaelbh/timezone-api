# Timezone API

## Overview

Timezone API is a simple web service that returns the current date and time considering a given time zone.

**Demo**: https://timezone-api-01.herokuapp.com/api/v1/docs

**Technologies used**
- python (flask, datetime, pytz)
- docker
- docker compose

TODO:
- open api
- github actions
- heroku

## Requirements
- docker: https://www.docker.com/
- docker-compose: https://docs.docker.com/compose/

## Setup (Local)

`$ docker-compose up -d`

## Setup (Remote)

`$ docker run -p 5000:5000 -d raphaelbh/timezone-api:latest`

## Testing

`http://localhost:5000/api/v1/docs`