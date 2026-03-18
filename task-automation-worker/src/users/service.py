import csv

import requests

from src.core.config import USERS_API_URL, DATA_PATH


class UsersService:
    def __init__(self, api_url: str = USERS_API_URL, data_path: str = DATA_PATH):
        self.api_url = api_url
        self.data_path = data_path

    def fetch_users(self) -> list:
        response = requests.get(self.api_url, timeout=10)
        response.raise_for_status()
        return response.json()

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
        normalized_data = self.normalize_users(users)
        with open(self.data_path, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "name", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(normalized_data)

    def fetch_and_save(self):
        users = self.fetch_users()
        self.save_users_to_csv(users)
