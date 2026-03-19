import logging

from src.users.service import UsersService
from src.core.celery import celery_app

logger = logging.getLogger(__name__)


@celery_app.task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 3})
def fetch_and_save_users():
    try:
        service = UsersService()
        service.fetch_and_save()
    except Exception:
        logger.exception("Failed to fetch and save users")
        raise
