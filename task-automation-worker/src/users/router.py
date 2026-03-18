from fastapi import APIRouter

from src.users.tasks import fetch_and_save_users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/fetch-users")
def fetch_users():
    task = fetch_and_save_users.delay()
    return {"task_id": task.id, "status": "started"}
