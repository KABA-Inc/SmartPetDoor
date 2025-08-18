import logging.config

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, user
from utils import db_migration
from utils.logging_config import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

logger.info("Running databse migrator...")
db_migration.run()

logger.info("Starting up backend...")
app = FastAPI()

logger.info("Attaching routers...")
app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
