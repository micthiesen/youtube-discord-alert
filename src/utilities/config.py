import json
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


class HistoryProvider(str, Enum):
    JSON = "JSON"


class Settings(BaseSettings):
    log_level: LogLevel = LogLevel.INFO
    poll_interval: int = 300
    channel_ids: List[str] = []
    discord_webhook: str
    youtube_api_key: str
    latest_channel_videos_count: int = 10
    max_history_per_channel: int = 20

    history_provider: HistoryProvider = HistoryProvider.JSON

    @property
    def log_level_parsed(self) -> int:
        return getattr(logging, self.log_level.value)

    def to_string(self, line_prefix: str = "") -> str:
        sensitive_keys = {"discord_webhook", "youtube_api_key"}
        return "\n".join(
            f"{line_prefix}{key.upper()}: {json.dumps(value)}"
            for key, value in self
            if key not in sensitive_keys
        )


CONFIG = Settings()
