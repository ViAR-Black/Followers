from app.core import db_connection

async def get_db_session():
    async with db_connection.session() as conn:
        yield conn

async def get_db_transaction():
    async with db_connection.transaction() as conn:
        yield conn