# from fastapi import APIRouter
# from app.core.db import user_db
# from app.services.password_hash import PasswordEncription

# user_router = APIRouter()
# @user_router.get('/me')
# async def get_user_info(login: str) -> str:
#     current = user_db.get(login, 'Неверный логин')
#     return str(current)

# @user_router.post('/sign_up')
# async def user_reg(login: str, password: str) -> str:
#     if user_db.get(login):
#         return 'Вы уже зарегистрированы'
#     encript = PasswordEncription(password)
#     user_db[login] = encript.hash_password()
#     return 'Вы зарегистрировать'