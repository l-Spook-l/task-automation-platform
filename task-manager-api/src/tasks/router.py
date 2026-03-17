from fastapi import APIRouter, Depends, status, HTTPException

from src.tasks.dependencies import get_task_service
from src.tasks.schemas import TaskCreate, TaskUpdate, TaskResponse
from src.tasks.service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("/tasks", response_model=list[TaskResponse])
def get_task(
        service: TaskService = Depends(get_task_service)
):
    return service.get_tasks()


@router.post("/tasks", response_model=TaskCreate)
def create_task(
        new_task: TaskCreate,
        service: TaskService = Depends(get_task_service)
):
    return service.create_task(new_task)


@router.put("/tasks/{task_id}")
async def update_task(task_id, update_data):
    pass


@router.delete("/tasks/{task_id}")
async def delete_task(task_id):
    pass
