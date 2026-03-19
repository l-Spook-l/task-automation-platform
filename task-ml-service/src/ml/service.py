import os
import joblib

from src.ml.config import MODEL_PATH


class TaskPriorityMLService:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        if os.path.exists(MODEL_PATH):
            self.model = joblib.load(MODEL_PATH)
        else:
            raise Exception("Model not found. Train it first.")

    def predict_priority(self, description: str) -> str:
        return self.model.predict([description])[0]
