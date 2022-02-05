import logging
import traceback
from time import sleep

from apis.discord import notify_discord
from apis.youtube import get_latest_channel_videos
from config import CONFIG
from history.json import JsonHistory

LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=CONFIG.log_level_parsed)
LOGGER = logging.getLogger(__name__)


def execution_loop():
    history = JsonHistory()
    while True:
        for channel_id in CONFIG.channel_ids:
            try:
                check_for_updates(history, channel_id)
            except Exception:
                LOGGER.error(traceback.format_exc()[:-1])

        LOGGER.info(f"Sleeping for {CONFIG.poll_interval} seconds...")
        sleep(CONFIG.poll_interval)


def check_for_updates(history: JsonHistory, channel_id: str) -> None:
    LOGGER.info(f"Checking for updates on channel {channel_id}")
    history.ensure_channel_exists(channel_id)
    videos = get_latest_channel_videos(channel_id)
    for video in videos:
        video_id = video.snippet.resourceId.videoId
        published_at = video.snippet.publishedAt
        if history.video_before_channel_added(channel_id, published_at):
            continue
        if history.video_already_seen(channel_id, video_id):
            continue
        notify_discord(video)
        history.mark_video_as_seen(channel_id, video_id)


if __name__ == "__main__":
    LOGGER.info("Using config: %s", CONFIG)
    LOGGER.info("Starting execution loop...")
    execution_loop()
