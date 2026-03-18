from fastapi import APIRouter


router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/fetch-users")
def fetch_users():
    pass
