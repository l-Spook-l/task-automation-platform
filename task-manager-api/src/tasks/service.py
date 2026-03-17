from typing import Dict

from src.tasks.schemas import TaskResponse, TaskCreate, TaskUpdate


class TaskService:
    def __init__(self):
        self.tasks: Dict[int, TaskResponse] = {}
        self.task_id_counter: int = 1

    def get_tasks(self) -> dict:
        pass

    def create_task(self, data: TaskCreate) -> dict:
        pass

    def update_task(self, task_id: int, data: TaskUpdate) -> dict:
        pass

    def delete_task(self, task_id: int) -> dict:
        pass
