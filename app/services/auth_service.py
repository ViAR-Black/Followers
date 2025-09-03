from app.repo.auth_repo import AuthRepo
from app.core.models.pydantic_models import RegisterUser, LoginUser
from app.core.custom_except import *

class RegisterService:
    def __init__(self, auth_repo:AuthRepo) -> None:
        self.auth_repo = auth_repo

    async def __call__(self, reg_model: RegisterUser) -> str:
        """Проверяет данные пользователя. Если всё ок
        регистрирует и выводит SUCCESS"""
        if await self.auth_repo.check_up_user(reg_model):
            raise AlreadyExists
        if '@' not in reg_model.mail:
            raise AvailableMailExeption
        if reg_model.password in ['12345', 'qwerty', '123455']:
            raise SimplePasswordExeption
        await self.auth_repo.sing_up(reg_model)
        return 'SUCCESS'
    
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