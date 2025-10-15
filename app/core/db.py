from contextlib import asynccontextmanager
from typing import AsyncIterator
from psycopg import AsyncConnection
from psycopg_pool import AsyncConnectionPool


class DatabaseConnection:    
    def __init__(self, max_pool_size, min_pool_size, db_connect_url):
        self.pool = AsyncConnectionPool(
            conninfo=db_connect_url,
            min_size=min_pool_size,
            max_size=max_pool_size,
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

    async def open(self):
        await self.pool.open()

    async def close(self):
        await self.pool.close()
