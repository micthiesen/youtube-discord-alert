from abc import ABC, abstractmethod


class BaseHistory(ABC):
    @abstractmethod
    def ensure_channel_exists(self, channel_id: str) -> None:
        """
        Ensure the channel exists in the history & mark first seen date if necessary
        """

    @abstractmethod
    def video_before_channel_first_seen(
        self, channel_id: str, video_published_at_str: str
    ) -> bool:
        """
        Return whether or not the video is from before the channel was first seen
        """

    @abstractmethod
    def video_already_seen(self, channel_id: str, video_id: str) -> bool:
        """
        Return whether or not the video has already been seen
        """

    @abstractmethod
    def mark_video_seen(self, channel_id: str, video_id: str) -> None:
        """
        Mark the video as seen in the history
        """
