from pydantic import BaseModel


class TaskRequest(BaseModel):
    description: str


class TaskPriorityResponse(BaseModel):
    task: str
    predicted_priority: str
