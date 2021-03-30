from celery import Celery

celery_app = Celery('celery_app', backend='redis://redis:6379/0', broker='redis://redis:6379/0')

from . import calculation
