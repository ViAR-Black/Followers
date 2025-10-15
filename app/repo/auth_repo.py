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
# Исправлена опечатка
    async def sign_in(self, login_model: LoginUser) -> bool:
        return True
    
# Отредактировал функцию (запрос к бд вместо auth_dict)
    async def is_user_exist(self, user_model:RegisterUser) -> bool:
        query = 'SELECT id FROM "user" WHERE email = %s'
        cursor = await self.connection.execute(query, (user_model.email,))
        check = await cursor.fetchone()
        if check is None:
            return False
        return True