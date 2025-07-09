from pydantic import BaseModel, EmailStr


class UserModel(BaseModel):
    """
    Internal representation of a user row as it lives in the database.
    Use this model *inside* the repository / service layer only.
    """

    id: str
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
