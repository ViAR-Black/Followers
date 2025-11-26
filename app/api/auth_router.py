from fastapi import APIRouter, Depends
from app.core.dependencies import get_db_session, get_db_transaction
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.services import RegisterService, LoginService
from app.repo import AuthRepo
from app.core.exceptions.custom_auth_except import *

from app.core.exceptions.http_exception import *
from psycopg import AsyncConnection


sign_router = APIRouter()

# Более читаемые названия, мелкие фиксы
@sign_router.post('/register')
async def sign_up(
    reg_model: RegisterUser,
    conn: AsyncConnection = Depends(get_db_transaction)
):
    try:
        auth_repo = AuthRepo(connection=conn)
        register_service = RegisterService(auth_repo=auth_repo)
        user_id = await register_service.register(reg_model=reg_model)
        return user_id
    except UserAlreadyExists:
        raise user_already_exist
    
@sign_router.post("/login")
async def login(
    login_data: LoginUser,
    conn: AsyncConnection = Depends(get_db_session)
):
    try:
        auth_repo = AuthRepo(connection=conn)
        login_service = LoginService(auth_repo=auth_repo)
        user_id = await login_service.login(login_data.email, login_data.password)
        return {"user_id": str(user_id)}
    except InvalidCredentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
