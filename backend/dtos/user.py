from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    password: str


class UserDTO(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
    username: str


class UserLoginDTO(BaseModel):
    username: str
    password: str
