from pydantic import BaseModel, EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponse(BaseModel):
    token: str

class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserRegisterResponse(BaseModel):
    name: str
    email: EmailStr