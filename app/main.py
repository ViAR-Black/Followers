from fastapi import FastAPI
# Исправлена опечатка
from app.api import sign_router
from app.core import db_connection
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    await db_connection.open()
    yield
    await db_connection.close()

def init_routers(app:FastAPI) -> None:
    # Исправлена опечатка
    app.include_router(sign_router)

def setup_app() -> FastAPI:
    app = FastAPI(
        title='My internet',
        description='Offline internet for you!',
        version='0.0.1',
        lifespan=lifespan
    )
    init_routers(app)
    return app


