import os


class Config:
    LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")

    class AuthToken:
        SECRET_KEY = os.getenv("TOKEN_SECRET_KEY", "secret")
        ALGORITHM = os.getenv("TOKEN_ALGORITHM", "HS256")
        EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES", "60"))

    class DB:
        HOST = os.getenv("DB_HOST", "localhost")
        DATABASE = os.getenv("DB_DATABASE", "smartpetdoor")
        USER = os.getenv("DB_USER", "root")
        PASSWORD = os.getenv("DB_PASSWORD", "pass")
        PORT = int(os.getenv("DB_PORT", "3306"))
