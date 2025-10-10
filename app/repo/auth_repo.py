from app.core.models.pydantic_models import RegisterUser, LoginUser
from psycopg import AsyncConnection

class AuthRepo:
    def __init__(self, connection: AsyncConnection)  -> None:
        self.connection = connection

    async def create_user(self, user_model: RegisterUser, password_hash: str) -> int:
        query = """ 
        INSERT INTO "user" (email, name, password_hash)
        VALUES (%s,%s,%s)
        RETURNING id
        """
        cursor = await self.connection.execute(query, (user_model.email, user_model.name, password_hash))
        user_id = (await cursor.fetchone())[0]
        return user_id

    async def sing_in(self, login_model: LoginUser) -> bool:
        return True
    
    async def check_up_user(self, user_model:RegisterUser) -> bool:
        if self.auth_dict.get(user_model.mail):
            return True
        return False
