from string import punctuation
from pydantic import BaseModel, Field, field_validator, EmailStr
from app.core.exceptions.custom_auth_except import *
from typing import Optional

# Сделал адекватную проверку email через EmailStr
# Ещё исправил опечатки
class RegisterUser(BaseModel):
    email: EmailStr
    name: str = Field(..., max_length=40)
    password: str = Field(..., max_length=250)
    # age и description — не обязательны при регистрации
    age: Optional[int] = None
    description: Optional[str] = Field(None, max_length=150)

    # Валидация возраста (если передан)
    @field_validator('age')
    @classmethod
    def validate_age(cls, v):
        if v is not None and not (0 <= v <= 100):
            raise ValueError('Age must be between 0 and 100')
        return v
    
    # Читаемость и оптимизация присоеденились к беседе)
    @field_validator('password')
    @classmethod
    def validate_password(cls, password: str) -> str:
        if len(password) < 8:
            raise ShortPwd()

        weak = {"qwerty", "123456", "000000", "password", "12345678"}
        if password.lower() in weak:
            raise WeakPwd()

        if not any(c.islower() for c in password):
            raise LowercasePwd()
        if not any(c.isupper() for c in password):
            raise UppercasePwd()
        if not any(c.isdigit() for c in password):
            raise WithoutDigitsPwd
        if not any(c in punctuation for c in password):
            raise WithoutPunctuationPwd()

        return password
    

class LoginUser(BaseModel):
    email: str
    password: str


class UserPlace(BaseModel):
    age: int
    name: str
    last_name: str

class UpdateUser(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    description: Optional[str] = None
    