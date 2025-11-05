from pydantic import BaseModel, field_validator
from string import punctuation

class RegisterUser(BaseModel):
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
    

class LoginUser(BaseModel):
    email: str
    password: str


class UserPlace(BaseModel):
    age: int
    nickname: str
    name: str
    last_name: str


    