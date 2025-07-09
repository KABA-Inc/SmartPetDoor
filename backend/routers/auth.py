from fastapi import APIRouter

router = APIRouter()


@router.get("/login")
def login():
    return "Login logic goes here..."


@router.get("/register")
def register():
    return "Register logic goes here..."
