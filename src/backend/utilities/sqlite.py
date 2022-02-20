import logging
import os
from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from sqlalchemy.sql import text

from models.base import Base
from utilities.config import CONFIG, LogLevel


MODULE_DIR = os.path.dirname(__file__)
MIGRATIONS_DIR = os.path.join(MODULE_DIR, "../migrations/")
ENGINE = create_engine(
    f"sqlite:///{CONFIG.sqlite_db_file}",
    echo=CONFIG.log_level == LogLevel.DEBUG,
    poolclass=NullPool,
)
LOGGER = logging.getLogger(__name__)


def initialize_db() -> None:
    LOGGER.debug("Initializing SQLite database")
    Base.metadata.create_all(ENGINE)
    run_migrations()


def run_migrations() -> None:
    Session = sessionmaker(bind=ENGINE)

    with Session.begin() as session:  # type: ignore
        current_version: int = session.execute("PRAGMA user_version").fetchone()[0]

    LOGGER.debug(f"Current migration version: {current_version}")
    migration_filenames = list(os.listdir(MIGRATIONS_DIR))
    LOGGER.debug(f"Loaded {len(migration_filenames)} migration files")

    for filename in sorted(migration_filenames):
        filepath = f"{MIGRATIONS_DIR}/{filename}"
        migration_version = get_migration_version(filename)
        if migration_version > current_version:
            LOGGER.info(f"Applying migration {migration_version}...")
            with Session.begin() as session, open(filepath, "r") as file:  # type: ignore
                query = text(file.read())
                session.execute(query)
                session.execute(f"PRAGMA user_version={migration_version}")
                LOGGER.info(f"Database now at version {migration_version}")
        else:
            LOGGER.debug(f"Migration {migration_version} already applied")


def get_migration_version(filename: str) -> int:
    return int(filename.split("_")[0])


def utc_aware(dt: datetime) -> datetime:
    """
    SQlite doesn't support timezone aware datetimes, so we need to convert them

    This is safe as all datetimes use UTC before being saved to the database.
    """
    return dt.replace(tzinfo=timezone.utc)
