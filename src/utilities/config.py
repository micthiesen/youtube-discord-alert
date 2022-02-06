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


class Entrypoint(str, Enum):
    WATCHER = "WATCHER"


class HistoryProvider(str, Enum):
    JSON = "JSON"
    SQLITE = "SQLITE"


class Settings(BaseSettings):
    log_level: LogLevel = LogLevel.INFO
    poll_interval: int = 300
    channel_ids: List[str] = []
    discord_webhook: str
    youtube_api_key: str
    latest_channel_videos_count: int = 10
    max_history_per_channel: int = 20

    # Currently undocumented settings
    entrypoint: Entrypoint = Entrypoint.WATCHER
    sqlite_db_file: str = "/data/db.sqlite3"
    history_provider: HistoryProvider = HistoryProvider.SQLITE
    history_json_file: str = "/data/history.json"

    @property
    def log_level_parsed(self) -> int:
        return getattr(logging, self.log_level.value)

    def to_string(self, line_prefix: str = "") -> str:
        sensitive_keys = {"discord_webhook", "youtube_api_key"}
        obfuscated = ", ".join(key.upper() for key, _ in self if key in sensitive_keys)
        non_obfuscated = "\n".join(
            f"{line_prefix}{key.upper()}: {json.dumps(value)}"
            for key, value in self
            if key not in sensitive_keys
        )
        return f"{non_obfuscated}\n{line_prefix}Hidden: {obfuscated}"


CONFIG = Settings()
