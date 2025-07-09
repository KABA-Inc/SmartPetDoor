import logging.config

from fastapi import FastAPI
from routers import auth
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
