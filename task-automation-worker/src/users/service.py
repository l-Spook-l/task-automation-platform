from src.users.utils import ApiManager, CsvManager


class UsersService:
    def __init__(self):
        self.api_manager = ApiManager()
        self.csv_manager = CsvManager()

    def fetch_and_save(self):
        users = self.api_manager.fetch_users()
        self.csv_manager.save_users_to_csv(users)
