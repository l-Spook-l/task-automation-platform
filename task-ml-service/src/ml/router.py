from fastapi import APIRouter, Depends, HTTPException

from src.ml.dependencies import get_ml_service
from src.ml.schemas import TaskRequest, TaskPriorityResponse
from src.ml.service import TaskPriorityMLService

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/predict", response_model=TaskPriorityResponse)
def predict(
        task: TaskRequest,
        service: TaskPriorityMLService = Depends(get_ml_service)
):
    try:
        prediction = service.predict_priority(task.description)

        return TaskPriorityResponse(
            task=task.description,
            predicted_priority=prediction
        )

    except Exception:
        raise HTTPException(status_code=500, detail="Prediction failed")
