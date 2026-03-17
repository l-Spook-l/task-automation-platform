from fastapi import APIRouter


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.post("/tasks")
async def create_task(new_task):
    pass


@router.get("/tasks")
async def get_task():
    pass


@router.put("/tasks/{task_id}")
async def update_task(task_id, update_data):
    pass


@router.delete("/tasks/{task_id}")
async def delete_task(task_id):
    pass
