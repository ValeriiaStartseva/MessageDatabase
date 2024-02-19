from fastapi import FastAPI, APIRouter
from tortoise.contrib.fastapi import register_tortoise
from handlers import users_router


app = FastAPI()

router = APIRouter(prefix="/api/v0")
router.include_router(users_router)
app.include_router(router)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True,
)
