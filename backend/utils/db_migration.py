import logging
from time import time

from retry import retry
from utils.config import Config
from yoyo import get_backend, read_migrations

logger = logging.getLogger(__name__)


@retry(Exception, tries=5, delay=2, backoff=2)
def apply_migration():

    config = Config.DB
    connection_string = "mysql://{user}:{password}@{host}:{port}/{dbname}".format(
        host=config.HOST,
        user=config.USER,
        password=config.PASSWORD,
        port=config.PORT,
        dbname=config.DATABASE,
    )

    backend = get_backend(connection_string, migration_table="yoyo_migrations_tasks")
    migrations = read_migrations("./migrations")
    backend.apply_migrations(backend.to_apply(migrations))


def run():
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting database migration...")

    # Start and measure database migration
    start_time = time()
    apply_migration()
    end_time = time()

    logger.info("Migration finished in %.3f seconds!" % (end_time - start_time))
