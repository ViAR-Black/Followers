from fastapi import FastAPI
from app.api import sing_router


def init_routers(app:FastAPI) -> None:
    app.include_router(sing_router)

def setup_app() -> FastAPI:
    app = FastAPI(
        title='My internet',
        description='Offline internet for you!',
        version='0.0.1'
    )
    init_routers(app)
    return app


