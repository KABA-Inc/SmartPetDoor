from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserDTO(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: EmailStr
