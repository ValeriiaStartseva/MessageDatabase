from fastapi import HTTPException, APIRouter
from models import Users_Pydantic, Users, Posts, Posts_Pydantic


users_router = APIRouter(prefix="/auth")


# Хендлер, який асинхронно запитуватиме дані з БД про всіх користувачів.
@users_router.get("/users/", response_model=list[Users_Pydantic], tags=["Users"])
async def get_all_users():
    users = await Users.all()
    return users


# Хендлер, який асинхронно запросить дані користувача з конкретним ID
@users_router.get("/users/{user_id}", response_model=Users_Pydantic, tags=["Users"])
async def get_user(user_id: int):
    user = await Users.filter(id=user_id).first()
    if user:
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")


# Хендлер, який асинхронно запитуватиме дані з БД про всі повідомлення користувача з конкретним ID.
@users_router.get("/posts/{user_id}", response_model=list[Posts_Pydantic], tags=["Posts"])
async def get_post_by_user_id(user_id: int):
    posts = await Posts.filter(user_id=user_id).all()
    if posts:
        return posts
    else:
        raise HTTPException(status_code=404, detail="Posts with this user_id is not found")
