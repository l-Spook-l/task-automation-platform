import uvicorn
from fastapi import FastAPI

from src.users.router import router as router_user

app = FastAPI(
    title="Task automation worker",
)

app.include_router(router_user, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, host="0.0.0.0", reload=True)
