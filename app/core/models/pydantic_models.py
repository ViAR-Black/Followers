from pydantic import BaseModel

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


    