from fastapi import APIRouter
from app.services.password_hash import PasswordEncription
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.services import RegisterService, LoginService
from app.repo import AuthRepo
from app.core.db import dictionary
from app.core.custom_except import *
from app.core.exception import *

sing_router = APIRouter()

@sing_router.post('/sing_up')
async def sing_up(reg_model: RegisterUser):
    try:
        print(dictionary)
        repo = AuthRepo(dictionary)
        reg_service = RegisterService(repo)
        await reg_service(reg_model)
    except SimplePasswordExeption:
        raise email_password_not_correct
    except AvailableMailExeption:
        raise email_password_not_correct
    except AlreadyExists:
        raise user_alreade_exist
    

@sing_router.post('/sing_in')
async def sing_in(log_model: LoginUser):
    repo = AuthRepo(dictionary)
    login_service = LoginService(repo)
    await login_service(log_model)