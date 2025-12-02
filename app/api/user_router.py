from fastapi import APIRouter, Depends
from app.core.db import user_db
from app.services.password_hash import PasswordEncription
from app.core.models.pydantic_models import UpdateUser
from psycopg import AsyncConnection
from app.core.dependencies import get_db_transaction

user_router = APIRouter()

#

@user_router.patch('/me')
async def update_user(
    user_model: UpdateUser,
    conn: AsyncConnection = Depends(get_db_transaction)
):
    # 1) Создать репозиторий или методы в репозитории для работы с бд
    # 2) Обернуть в сервис
    # 3) Подумать над вариантами ошибок
    # 4) Посмотреть  model_dump(exclude_unset=True) - Pydantic
    pass




# @user_router.get('/me')
# async def get_user_info(login: str) -> str:
#     current = user_db.get(login, 'Неверный логин')
#     return str(current)


