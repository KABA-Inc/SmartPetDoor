import logging

from dtos.user import UserCreateDTO, UserLoginDTO
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.auth import auth_service

logger = logging.getLogger(__name__)

router = APIRouter()


class SuccessfulLoginResponse(BaseModel):
    token: str


class SuccessfulRegisterResponse(BaseModel):
    description: str
    id: str


@router.post("/login", response_model=SuccessfulLoginResponse, status_code=200)
def login(user: UserLoginDTO):
    logger.debug(f"Logging in {user.username} user")

    try:
        return SuccessfulLoginResponse(token=auth_service.login(user))
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/register", response_model=SuccessfulRegisterResponse, status_code=201)
def register(user: UserCreateDTO):
    logger.debug("Registering...")

    try:

        created_user = auth_service.register(user)

        return SuccessfulRegisterResponse(
            description="User created successfuly!", id=created_user.id
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
