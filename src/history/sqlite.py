import logging

from history.base import BaseHistory


LOGGER = logging.getLogger(__name__)


class SqliteHistory(BaseHistory):
    def ensure_channel_exists(self, channel_id: str) -> None:
        pass

    def video_before_channel_first_seen(
        self, channel_id: str, video_published_at_str: str
    ) -> bool:
        pass

    def video_already_seen(self, channel_id: str, video_id: str) -> bool:
        pass

    def mark_video_seen(self, channel_id: str, video_id: str) -> None:
        pass
