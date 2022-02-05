import logging
from typing import Any

import requests
from pyyoutube import PlaylistItem
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from utilities.config import CONFIG


LOGGER = logging.getLogger(__name__)
YT_VIDEO_URL = "https://www.youtube.com/watch?v={0}"
YT_CHANNEL_URL = "https://www.youtube.com/channel/{0}"


def notify_discord(video: PlaylistItem) -> None:
    LOGGER.info('Sending notification for video "%s"', video.snippet.title)
    response = _post_with_retry(
        CONFIG.discord_webhook,
        json={
            "content": (
                f"New upload from {video.snippet.channelTitle}: "
                f"{YT_VIDEO_URL.format(video.snippet.resourceId.videoId)}"
            ),
        },
    )
    response.raise_for_status()


def _post_with_retry(url: str, **kwargs: Any) -> requests.Response:
    session = requests.Session()
    retries = Retry(
        total=5,
        backoff_factor=1,
        respect_retry_after_header=False,
        status_forcelist=[429],
        allowed_methods=[*Retry.DEFAULT_ALLOWED_METHODS, "POST"],
    )
    session.mount("https://", HTTPAdapter(max_retries=retries))
    return session.post(url, **kwargs)
