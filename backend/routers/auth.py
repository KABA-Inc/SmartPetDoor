import logging

from fastapi import APIRouter

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/login")
def login():
    logger.debug("Logging in...")
    return "Login logic goes here..."


@router.get("/register")
def register():
    logger.debug("Registering...")
    return "Register logic goes here..."
