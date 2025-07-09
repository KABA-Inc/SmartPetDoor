from datetime import datetime, timedelta

import jwt
from dtos.user import UserCreateDTO, UserDTO, UserLoginDTO
from repositories.mysql import MySQL
from services.user import user_service
from utils.config import Config


class AuthService:
    def __init__(self) -> None:
        self.repository = MySQL()

    def _generate_token(self, user_id: str) -> str:
        expire = datetime.utcnow() + timedelta(minutes=Config.AuthToken.EXPIRE_MINUTES)
        payload = {
            "sub": user_id,
            "exp": expire,
            "iat": datetime.utcnow(),
        }
        token = jwt.encode(
            payload, Config.AuthToken.SECRET_KEY, algorithm=Config.AuthToken.ALGORITHM
        )
        return token

    def register(self, user: UserCreateDTO) -> UserDTO:
        return user_service.create_user(user)

    def login(self, user: UserLoginDTO):
        found_user = self.repository.get_user(username=user.username)

        if not found_user:
            raise Exception(f"User does not found with username {user.username}")

        passwords_match = found_user.password == user_service.hash_password(
            user.password
        )
        if not passwords_match:
            raise Exception("Wrong password!")

        token = self._generate_token(found_user.id)
        return token


auth_service = AuthService()
