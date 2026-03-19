from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    description: str = Field(min_length=3)


class TaskPriorityResponse(BaseModel):
    task: str
    predicted_priority: str
