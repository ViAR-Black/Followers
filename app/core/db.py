from contextlib import asynccontextmanager
from typing import AsyncIterator
from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool


class DatabaseConnection:    
    def __init__(self, settings):
        self.pool = AsyncConnectionPool(
            conninfo=settings.database.db_uri,
            min_size=settings.database.min_pool_size,
            max_size=settings.database.max_pool_size,
        )
    
    @asynccontextmanager
    async def session(self) -> AsyncIterator[AsyncConnection]:
        async with self.pool.connection() as conn:
            yield conn
    
    @asynccontextmanager
    async def transaction(self) -> AsyncIterator[AsyncConnection]:
        async with self.pool.connection() as conn:
            async with conn.transaction():
                yield conn
