from fastapi import FastAPI
from routers import calculation

app = FastAPI(
    title="FastAPI / Celery POC",
    description="Very simple HTTP API to demonstrate how to handle CPU bound tasks using Celery and FastAPI.",
    version="0.0.1"
)


app.include_router(calculation.router, prefix="/api")
