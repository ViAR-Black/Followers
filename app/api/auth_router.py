from fastapi import APIRouter, Depends
from app.core.dependencies import get_db_transaction
from app.services.password_hash import PasswordEncription
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.services import RegisterService, LoginService
from app.repo import AuthRepo
# from app.core.db import dictionary
from app.core.custom_except import *

from app.core.exception import *
from psycopg import AsyncConnection
# Исправлена опечатка
sign_router = APIRouter()

# Исправлены опечатки и добавлен return
@sign_router.post('/sign_up')
async def sign_up(
    reg_model: RegisterUser,
    conn: AsyncConnection = Depends(get_db_transaction)
):
    try:
        auth_repo = AuthRepo(connection=conn)
        register_service = RegisterService(auth_repo=auth_repo)
        user_id = await register_service(reg_model=reg_model)
        return user_id
    except UserAlreadyExists:
        raise user_already_exist


        





    # try:
    #     print(dictionary)
    #     repo = AuthRepo(dictionary)
    #     reg_service = RegisterService(repo)
    #     await reg_service(reg_model)
    #     # Добавлен return
    #     return f"{reg_model.name}, вы успешно зарегистрированы."
    
    # except SimplePasswordExeption:
    #     raise email_password_not_correct
    # except AvailableMailExeption:
    #     raise email_password_not_correct
    # except AlreadyExists:
    #     # Исправлена опечатка
    #     raise user_already_exist
    
    
#Исправлена опечатка
@sign_router.post('/sign_in')
async def sign_in(log_model: LoginUser):
    repo = AuthRepo(dictionary)
    login_service = LoginService(repo)
    await login_service(log_model)