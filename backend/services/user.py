import uuid
from typing import List

from dtos.user import UserCreateDTO, UserDTO
from models.user import UserModel
from repositories.mysql import MySQL


class UserService:
    def __init__(self) -> None:
        self.repository = MySQL()

    def get_all_user(self) -> List[UserDTO]:
        users = self.repository.get_all_user()
        return [UserDTO(**u.model_dump()) for u in users]

    def get_user(self, id: str) -> UserDTO | None:
        user = self.repository.get_user(id)
        if user is None:
            return None
        return UserDTO(**user.model_dump())

    def create_user(self, user: UserCreateDTO) -> UserDTO | None:
        user_model = UserModel(id=str(uuid.uuid4()), **user.model_dump())
        affected_rows = self.repository.create_user(user_model)

        if affected_rows > 0:
            return self.get_user(user_model.id)
        return None


user_service = UserService()
