from fastapi import FastAPI
# Исправлена опечатка
from app.api import sign_router


def init_routers(app:FastAPI) -> None:
    # Исправлена опечатка
    app.include_router(sign_router)

def setup_app() -> FastAPI:
    app = FastAPI(
        title='My internet',
        description='Offline internet for you!',
        version='0.0.1'
    )
    init_routers(app)
    return app


