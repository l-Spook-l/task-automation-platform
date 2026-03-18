import os

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
USERS_API_URL = "https://jsonplaceholder.typicode.com/users"
DATA_PATH = "/app/data/users.csv"
