from fastapi import APIRouter, Depends, status, HTTPException

from src.tasks.dependencies import get_task_service
from src.tasks.schemas import TaskCreate, TaskUpdate, TaskResponse
from src.tasks.service import TaskService

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)


@router.get("", response_model=list[TaskResponse])
def get_task(
        service: TaskService = Depends(get_task_service)
):
    return service.get_tasks()


@router.post("", response_model=TaskCreate)
def create_task(
        new_task: TaskCreate,
        service: TaskService = Depends(get_task_service)
):
    return service.create_task(new_task)


@router.put("/{task_id}")
def update_task(
        task_id: int,
        update_data: TaskUpdate,
        service: TaskService = Depends(get_task_service)
):
    task = service.update_task(task_id, update_data)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
        task_id: int,
        service: TaskService = Depends(get_task_service)
):
    task = service.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
