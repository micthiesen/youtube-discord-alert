from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    poll_interval: int = 60
    channel_ids: List[str] = []
    youtube_api_key: str
    latest_channel_videos_count: int = 10
    max_history_per_channel: int = 20


CONFIG = Settings()
