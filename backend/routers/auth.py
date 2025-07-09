import logging

from dtos.user import UserCreateDTO
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.user import user_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/login")
def login():
    logger.debug("Logging in...")
    return "Login logic goes here..."


@router.post("/register")
def register(user: UserCreateDTO):
    logger.debug("Registering...")

    created_user = user_service.create_user(user)

    if created_user:
        return JSONResponse(content="User created successfuly!", status_code=203)
    else:
        return JSONResponse(content="Error occured.", status_code=400)
