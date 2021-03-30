from services import calculation
from tasks import celery_app


@celery_app.task
def long_add(a: int, b: int):
    return calculation.long_add(a, b)
