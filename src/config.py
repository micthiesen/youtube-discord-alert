from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    poll_interval: int = 60
    channel_ids: List[int] = []


CONFIG = Settings()
