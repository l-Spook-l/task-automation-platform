import os

import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from src.ml.config import CSV_PATH, MODEL_PATH, MODEL_DIR

MODEL_DIR.mkdir(parents=True, exist_ok=True)


def train_model(csv_path="tasks.csv", model_path="model.joblib"):
    """
    Train a simple text classification model to predict task priority.

    Args:
        csv_path (str): Path to the input CSV file with tasks.
        model_path (str): Path where the trained model will be saved.
    """

    # 1. Load dataset
    df = pd.read_csv(csv_path)

    # 2. Split features and target
    X = df["task_description"]
    y = df["priority"]

    # 3. Create pipeline: text vectorization + classifier
    model = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression())
    ])

    # 4. Train model
    model.fit(X, y)

    # 5. Save trained model
    joblib.dump(model, model_path)

    print(f"Model trained and saved to: {model_path}")


if __name__ == "__main__":
    train_model(csv_path=CSV_PATH, model_path=MODEL_PATH)
