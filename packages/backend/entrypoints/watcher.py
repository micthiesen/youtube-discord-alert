import logging
import traceback
from time import sleep

from history import BaseHistory, get_history_from_config
from services.discord import notify_discord
from services.youtube import get_latest_channel_videos
from utilities.config import CONFIG
from utilities.youtube import parse_youtube_datetime


LOGGER = logging.getLogger(__name__)


def entrypoint() -> None:
    LOGGER.info("Starting watcher...")
    history = get_history_from_config()
    while True:
        for channel_id in CONFIG.channel_ids:
            try:
                _check_for_updates(history, channel_id)
            except Exception:
                LOGGER.error(traceback.format_exc()[:-1])

        LOGGER.info(f"Sleeping for {CONFIG.poll_interval} seconds...")
        sleep(CONFIG.poll_interval)


def _check_for_updates(history: BaseHistory, channel_id: str) -> None:
    LOGGER.info(f"Checking for updates on channel {channel_id}")
    history.ensure_channel_exists(channel_id)
    videos = get_latest_channel_videos(channel_id)
    for video in videos:
        video_id = video.snippet.resourceId.videoId
        published_at = parse_youtube_datetime(video.snippet.publishedAt)
        if history.video_before_channel_first_seen(channel_id, published_at):
            continue
        if history.video_already_seen(channel_id, video_id):
            continue
        notify_discord(video)
        history.mark_video_notified(channel_id, video_id)
