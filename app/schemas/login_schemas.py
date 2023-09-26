from pydantic import BaseModel, EmailStr


class LoginCredentials(BaseModel):
    user_name: str | EmailStr
    password: str


class PayloadCredentials(BaseModel):
    user_name: str
    role: str


class ChangePasswordCredentials(BaseModel):
    user_name: str | EmailStr
    password: str
    new_password: str
    repeat_password: str
