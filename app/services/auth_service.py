from app.repo.auth_repo import AuthRepo
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.core.exceptions.custom_auth_except import *
from app.services.password_hash import hash_password, verify_password

class RegisterService:
    def __init__(self, auth_repo:AuthRepo) -> None:
        self.auth_repo = auth_repo

    # Переименовал с __call__ на register для читаемости
    async def register(self, reg_model: RegisterUser) -> str:
        """Проверяет данные пользователя. Если всё ок,
        регистрирует"""
         # Проверка существования
        if await self.auth_repo.is_user_exist(reg_model.email):
            raise UserAlreadyExists
        
        # Можно также удобно и легко добавить другие проверки...
        
        hashed = hash_password(reg_model.password)
        return await self.auth_repo.create_user(
            email=reg_model.email,
            name=reg_model.name,
            password_hash=hashed
            )

    
class LoginService:
    def __init__(self, auth_repo: AuthRepo):
        self.auth_repo = auth_repo

    async def login(self, email: str, password: str) -> str:  # возвращает user_id
        user = await self.auth_repo.get_user_hash_password(email)
        if not user or not verify_password(password, user["hashed_password"]):
            raise InvalidCredentials
        
        return user["id"]