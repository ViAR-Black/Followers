from pydantic import BaseModel
from typing import Optional

class RegisterUser(BaseModel):
    mail: str
    nickname: str
    password: str


class LoginUser(BaseModel):
    mail: str
    password: str


class UserPlace(BaseModel):
    age: int
    nickname: str
    name: str
    last_name: str


class PostRoom(BaseModel):
    title: str
    descript: str
    members: list[int]

class PatchRoom(BaseModel):
    title: Optional[str]
    descript: Optional[str]
    members: Optional[list[int]]

    