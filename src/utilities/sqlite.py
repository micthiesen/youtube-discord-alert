from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

from models.base import Base
from utilities.config import CONFIG, LogLevel


ENGINE = create_engine(
    f"sqlite:///{CONFIG.sqlite_db_file}",
    echo=CONFIG.log_level == LogLevel.DEBUG,
    poolclass=NullPool,
)


def initialize_db() -> None:
    Base.metadata.create_all(ENGINE)
