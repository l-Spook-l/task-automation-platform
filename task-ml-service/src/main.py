import uvicorn
from fastapi import FastAPI

from src.ml.router import router as router_ml

app = FastAPI(
    title="Prediction priority task",
)

app.include_router(router_ml, prefix="/api")

if __name__ == "__main__":
    uvicorn.run("src.main:app", port=8000, host="0.0.0.0", reload=True)
