import hashlib
import uuid
from typing import List

from dtos.user import UserCreateDTO, UserDTO
from models.user import UserModel
from repositories.mysql import MySQL


class UserService:
    def __init__(self) -> None:
        self.repository = MySQL()

    def hash_password(self, password: str):
        return hashlib.sha256(password.encode()).hexdigest()

    def get_all_user(self) -> List[UserDTO]:
        users = self.repository.get_all_user()
        return [UserDTO(**u.model_dump()) for u in users]

    def get_user(self, id=None, username=None) -> UserDTO | None:
        user = self.repository.get_user(id, username)
        if user is None:
            return None
        return UserDTO(**user.model_dump())

    def create_user(self, user: UserCreateDTO) -> UserDTO:
        existing_username = self.get_user(username=user.username)
        if existing_username:
            raise Exception("Username has already taken!")

        user_model = UserModel(id=str(uuid.uuid4()), **user.model_dump())
        user_model.password = self.hash_password(user_model.password)

        affected_rows = self.repository.create_user(user_model)

        if affected_rows == 0:
            raise Exception("Couldn't create user!")

        created_user = self.get_user(id=user_model.id)
        if not created_user:
            raise Exception("Couldn't find user!")

        return created_user


user_service = UserService()
