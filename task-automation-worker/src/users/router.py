from fastapi import APIRouter, HTTPException

from src.users.tasks import fetch_and_save_users

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/fetch-users")
def fetch_users():
    try:
        task = fetch_and_save_users.delay()
        return {"task_id": task.id, "status": "started"}
    except Exception:
        raise HTTPException(status_code=500, detail="Failed to start task")
