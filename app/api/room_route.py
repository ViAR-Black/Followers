from fastapi import APIRouter
from app.services.password_hash import PasswordEncription
from app.core.models.pydantic_models import RegisterUser, LoginUser, PostRoom, PatchRoom
from app.services import RegisterService, LoginService
from app.repo import AuthRepo
from app.core.db import dictionary
from app.core.custom_except import *
from app.core.exception import *

room_router = APIRouter()

@room_router.post('/room')
async def create_room(room_info: PostRoom):
    pass

@room_router.get('/room/{user_id}')
async def get_room(user_id: int):
    pass

@room_router.delete('/room')
async def delete_room(room_id: int):
    pass

@room_router.patch('/room')
async def patch_room(room_id: PatchRoom):
    pass