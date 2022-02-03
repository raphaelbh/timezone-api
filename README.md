# Timezone API

## Overview

Timezone API is a simple web service that returns the current date and time considering a given time zone.

**Swagger**: /swagger (???)

**Technologies used**
- python (flask, datetime, pytz)
- docker
- docker compose
- open api

## Requirements
- docker: https://www.docker.com/
- docker-compose: https://docs.docker.com/compose/

## Setup (Local)

`$ docker-compose up -d`

## Setup (Remote)

`$ docker run ... ???`

## Testing

`$ curl http://localhost:5000/api/v1/timezones`

`$ curl http://localhost:5000/api/v1/now`