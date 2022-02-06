import logging
from datetime import datetime, timezone

from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from models.base import Base
from utilities.config import CONFIG, LogLevel


ENGINE = create_engine(
    f"sqlite:///{CONFIG.sqlite_db_file}",
    echo=CONFIG.log_level == LogLevel.DEBUG,
    poolclass=NullPool,
)
LOGGER = logging.getLogger(__name__)


def initialize_db() -> None:
    LOGGER.debug("Initializing SQLite database")
    Base.metadata.create_all(ENGINE)


def utc_aware(dt: datetime) -> datetime:
    """
    SQlite doesn't support timezone aware datetimes, so we need to convert them

    This is safe as all datetimes use UTC before being saved to the database.
    """
    return dt.replace(tzinfo=timezone.utc)
