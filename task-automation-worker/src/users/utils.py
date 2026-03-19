import csv
import logging

import requests

from src.core.config import USERS_API_URL, DATA_PATH

logger = logging.getLogger(__name__)


class ApiManager:
    def __init__(self, api_url: str = USERS_API_URL):
        self.api_url = api_url

    def fetch_users(self) -> list:
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException:
            logger.exception("API request failed")
            raise


class CsvManager:
    def __init__(self, data_path: str = DATA_PATH):
        self.data_path = data_path

    @staticmethod
    def normalize_users(data: list) -> list:
        filtered_data = list()
        for user in data:
            filtered_data.append({
                "id": user.get("id"),
                "name": user.get("name"),
                "email": user.get("email"),
            })
        return filtered_data

    def save_users_to_csv(self, users: list) -> None:
        try:
            normalized_data = self.normalize_users(users)
            with open(self.data_path, "w", newline="", encoding="utf-8") as file:
                fieldnames = ["id", "name", "email"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(normalized_data)
        except Exception:
            logger.exception("Failed to save users to CSV")
            raise
