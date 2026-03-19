import uvicorn
from fastapi import FastAPI

from src.tasks.router import router as router_task

app = FastAPI(
    title="Task manager",
)

app.include_router(router_task, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, host="0.0.0.0", reload=True)
