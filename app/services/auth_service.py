from app.repo.auth_repo import AuthRepo
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.core.exceptions.custom_auth_except import *
from app.services.password_hash import PasswordEncription

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
        
        hashed = PasswordEncription.hash_password(reg_model.password)
        return await self.auth_repo.create_user(
            email=reg_model.email,
            name=reg_model.name,
            password_hash=hashed
            )

    
class LoginService:
    def __init__(self, auth_repo: AuthRepo):
        self.auth_repo = auth_repo

    async def __call__(self, login_model: LoginUser):
        if await self.auth_repo.check_up_user(login_model):
            current_user_model = self.auth_dict[login_model.mail]['auth']
            if current_user_model.password == login_model.password:
                return 'SUCCESS'
            else:
                raise 'WRONG PASSWORD'
        else:
            raise 'USER IS NOT FOUND'