import logging
from enum import Enum
from typing import List

from pydantic import BaseSettings


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Settings(BaseSettings):
    log_level: LogLevel = LogLevel.INFO
    poll_interval: int = 60
    channel_ids: List[str] = []
    discord_webhook: str
    youtube_api_key: str
    latest_channel_videos_count: int = 10
    max_history_per_channel: int = 20

    @property
    def log_level_parsed(self) -> int:
        return getattr(logging, self.log_level.value)


CONFIG = Settings()
