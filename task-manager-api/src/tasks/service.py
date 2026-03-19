import logging
from typing import Dict

from src.tasks.schemas import TaskResponse, TaskCreate, TaskUpdate

logger = logging.getLogger(__name__)


class TaskService:
    def __init__(self):
        self.tasks: Dict[int, TaskResponse] = {}
        self.task_id_counter: int = 1

    def get_tasks(self) -> list:
        return list(self.tasks.values())

    def create_task(self, data: TaskCreate) -> TaskResponse:
        task_id = self.task_id_counter

        task = TaskResponse(
            id=task_id,
            title=data.title,
            description=data.description,
            completed=data.completed
        )

        self.tasks[task_id] = task
        self.task_id_counter += 1

        return task

    def update_task(self, task_id: int, data: TaskUpdate) -> TaskResponse | None:
        if task_id not in self.tasks:
            return None

        task = self.tasks[task_id]
        update_data = data.model_dump(exclude_unset=True)
        updated_task = task.model_copy(update=update_data)
        self.tasks[task_id] = updated_task

        return updated_task

    def delete_task(self, task_id: int) -> TaskResponse | None:
        task = self.tasks.pop(task_id, None)
        if not task:
            logger.warning(f"Task {task_id} not found for deletion")
        return task
