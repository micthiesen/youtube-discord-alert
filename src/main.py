import logging
import traceback
from time import sleep

from config import CONFIG
from history import add_to_history, check_history
from youtube import get_latest_channel_videos


LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def execution_loop():
    while True:
        for channel_id in CONFIG.channel_ids:
            try:
                check_for_updates(channel_id)
            except Exception as err:
                LOGGER.error(traceback.format_exc()[:-1])

        LOGGER.info(f"Sleeping for {CONFIG.poll_interval} seconds...")
        sleep(CONFIG.poll_interval)


def check_for_updates(channel_id: str) -> None:
    LOGGER.info(f"Checking for updates on channel {channel_id}")
    videos = get_latest_channel_videos(channel_id)
    for video in videos:
        check_history(channel_id, video.snippet.resourceId.videoId)
        add_to_history(channel_id, video.snippet.resourceId.videoId)


if __name__ == "__main__":
    LOGGER.info("Using config: %s", CONFIG)
    LOGGER.info("Starting execution loop...")
    execution_loop()
