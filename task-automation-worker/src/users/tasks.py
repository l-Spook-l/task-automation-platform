from src.users.service import UsersService
from src.core.celery import celery_app


@celery_app.task
def fetch_and_save_users():
    service = UsersService()
    service.fetch_and_save()
