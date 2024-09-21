from fastapi import APIRouter

from src.database.user.schemas import NewUser, UserLogin, User
from src.database.user.service import user_service

user_router = APIRouter(prefix="/database/user")


@user_router.post("/create", status_code=201)
async def create(data: NewUser) -> None:
    await user_service.create_new_user(data)


@user_router.get("/login", status_code=200)
async def login(data: UserLogin) -> User:
    return await user_service.login_user(data)
