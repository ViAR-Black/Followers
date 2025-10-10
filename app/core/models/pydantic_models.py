from pydantic import BaseModel

class RegisterUser(BaseModel):
    email: str
    name: str
    password: str


class LoginUser(BaseModel):
    email: str
    password: str


class UserPlace(BaseModel):
    age: int
    nickname: str
    name: str
    last_name: str


    