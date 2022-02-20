import json
import logging
from enum import Enum
from typing import List, Literal

from pydantic import BaseSettings


CHANNEL_IDS_SQLITE = Literal["SQLITE"]


class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


class Entrypoint(str, Enum):
    WATCHER = "WATCHER"
    WEBSERVER = "WEBSERVER"
    WATCHER_AND_WEBSERVER = "WATCHER_AND_WEBSERVER"


class HistoryProvider(str, Enum):
    SQLITE = "SQLITE"


class Settings(BaseSettings):
    log_level: LogLevel = LogLevel.INFO
    poll_interval: int = 300
    channel_ids: List[str] | CHANNEL_IDS_SQLITE = []
    discord_webhook: str
    youtube_api_key: str
    latest_channel_videos_count: int = 10
    max_history_per_channel: int = 30

    # Currently undocumented settings
    entrypoint: Entrypoint = Entrypoint.WATCHER
    sqlite_db_file: str = "/data/db.sqlite3"
    history_provider: HistoryProvider = HistoryProvider.SQLITE
    webserver_port: int = 5777

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
