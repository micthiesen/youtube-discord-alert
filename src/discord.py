import logging

import requests
from pyyoutube import PlaylistItem

from config import CONFIG


LOGGER = logging.getLogger(__name__)
YT_VIDEO_URL = "https://www.youtube.com/watch?v={0}"
YT_CHANNEL_URL = "https://www.youtube.com/channel/{0}"


def notify_discord(video: PlaylistItem):
    LOGGER.info('Sending notification for video "%s"', video.snippet.title)
    response = requests.post(
        CONFIG.discord_webhook,
        json={
            "content": (
                f"New upload from {video.snippet.channelTitle}: "
                f"{YT_VIDEO_URL.format(video.snippet.resourceId.videoId)}"
            ),
        },
    )
    response.raise_for_status()