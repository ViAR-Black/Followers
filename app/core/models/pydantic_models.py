<<<<<<< HEAD
from string import punctuation
from pydantic import BaseModel, Field, field_validator, EmailStr
from app.core.exceptions.custom_auth_except import *
from typing import Optional
=======
from pydantic import BaseModel, field_validator
from string import punctuation
>>>>>>> main

# Сделал адекватную проверку email через EmailStr
# Ещё исправил опечатки
class RegisterUser(BaseModel):
<<<<<<< HEAD
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
=======
    email: str
    name: str
    password: str

    @field_validator('email')
    @classmethod
    def validate_email(cls, email: str):
        if len(email) <= 3:
            raise ValueError("Unavailable email")
        if '@' not in email:
            raise ValueError("Email must have a @ symbol")
        
        return email
    
    @field_validator('password')
    @classmethod
    def validate_password(cls, password):
        unavailable_passwords = [
            'qwerty',
            '123456',
            '000000'
        ]

        if len(password) < 6:
            raise ValueError("Your password in too short!")
        if password in unavailable_passwords:
            raise ValueError("Your password is too simple")
        
        punsctuation_flag = False
        upper_case_flag = False
        lower_case_flag = False
        digit_flag = False
        
        for char in password:
            if char in punctuation:
                punsctuation_flag = True
            elif char.isdigit():
                digit_flag = True
            elif char.isupper():
                upper_case_flag = True
            elif char.islower():
                lower_case_flag = True

        if all([punsctuation_flag, upper_case_flag, lower_case_flag, digit_flag]):
            return password
        raise ValueError("Uncorrect password.")
>>>>>>> main
    

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
    