import os
import joblib

from src.ml.config import MODEL_PATH


class TaskPriorityMLService:
    def __init__(self):
        self.model = self._load_model()

    @staticmethod
    def _load_model():
        if os.path.exists(MODEL_PATH):
            return joblib.load(MODEL_PATH)
        raise RuntimeError("Model not trained")

    def predict_priority(self, description: str) -> str:
        return self.model.predict([description])[0]
