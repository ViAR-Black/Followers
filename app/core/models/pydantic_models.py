from pydantic import BaseModel, Field

class RegisterUser(BaseModel):
    email: str = Field(..., le=75)
    name: str = Field(..., le=20)
    password: str = Field(..., le=250)
    


class LoginUser(BaseModel):
    mail: str
    password: str


class UserPlace(BaseModel):
    age: int
    nickname: str
    name: str
    last_name: str


    