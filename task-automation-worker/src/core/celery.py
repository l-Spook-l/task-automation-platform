from celery import Celery

from src.core.config import REDIS_URL

celery_app = Celery(
    "tasks",
    broker=REDIS_URL,
    backend=REDIS_URL,
)

celery_app.autodiscover_tasks(['src.users'])
