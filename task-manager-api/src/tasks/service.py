from typing import Dict

from src.tasks.schemas import TaskResponse, TaskCreate, TaskUpdate


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

    def update_task(self, task_id: int, data: TaskUpdate) -> dict:
        pass

    def delete_task(self, task_id: int) -> dict:
        pass
