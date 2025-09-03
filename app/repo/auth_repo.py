from app.core.models.pydantic_models import RegisterUser, LoginUser

class AuthRepo:
    def __init__(self, auth_dict: dict) -> None:
        self.auth_dict = auth_dict

    async def sing_up(self, user_model: RegisterUser) -> bool:
        self.auth_dict[user_model.mail] = {
            'auth': user_model
            }
        return True
    
    async def sing_in(self, login_model: LoginUser) -> bool:
        return True
    
    async def check_up_user(self, user_model:RegisterUser) -> bool:
        if self.auth_dict.get(user_model.mail):
            return True
        return False
