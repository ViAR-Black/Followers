from app.core.models.pydantic_models import RegisterUser, LoginUser
from psycopg import AsyncConnection

class AuthRepo:
    def __init__(self, connection: AsyncConnection)  -> None:
        self.connection = connection

    # Привел к минимализму - передаём только необходимое
    async def create_user(self, email: str, name: str, password_hash: str) -> int:
        query = """ 
        INSERT INTO "user" (email, name, password_hash)
        VALUES (%s,%s,%s)
        RETURNING id
        """
        cursor = await self.connection.execute(query, (email, name, password_hash))
        user_id = (await cursor.fetchone())[0]
        return user_id
    
    async def sign_in(self, login_model: LoginUser) -> bool:
        return True
    
    # Привел к минимализму - передаём только необходимое
    async def is_user_exist(self, email: str) -> bool:
        query = 'SELECT id FROM "user" WHERE email = %s'
        cursor = await self.connection.execute(query, (email,))
        check = await cursor.fetchone()
        if check is None:
            return False
        return True