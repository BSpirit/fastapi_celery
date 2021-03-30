# FastAPI, Celery POC

# Overview

The main purpose of this app is to demonstrate how to handle CPU bound tasks using [FastAPI](https://fastapi.tiangolo.com/) and [Celery](https://docs.celeryproject.org/en/stable/getting-started/introduction.html).

## Requirements

Docker and Docker compose can be used to run the application on your local machine.

1. Install [Docker](https://docs.docker.com/get-docker/)

2. Install [Docker compose](https://docs.docker.com/compose/install/)


## Run application
```
docker compose up
```

*The app listens on port 8000.*

Once the app is running, the automatic **interactive API documentation** can be accessed here:  http://127.0.0.1:8000/docs (provided by [Swagger UI](https://swagger.io/tools/swagger-ui/))
The interactive API documentation can be used to test the application.