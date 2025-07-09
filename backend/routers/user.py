import logging
from typing import List

from dtos.user import UserDTO
from fastapi import APIRouter
from services.user import user_service

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/", response_model=List[UserDTO])
def get_all():

    users = user_service.get_all_user()
    logger.debug(f"Fetched {len(users)} users.")
    return users
