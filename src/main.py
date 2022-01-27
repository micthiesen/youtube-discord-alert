import logging
from time import sleep

from config import CONFIG
from youtube import get_subscription_by_channel


LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def execution_loop():
    while True:
        for channel_id in CONFIG.channel_ids:
            try:
                check_for_updates(channel_id)
            except Exception as err:
                LOGGER.error(f"Error while checking for updates: {err}")

        LOGGER.info(f"Sleeping for {CONFIG.poll_interval} seconds...")
        sleep(CONFIG.poll_interval)


def check_for_updates(channel_id: str) -> None:
    subscriptions = get_subscription_by_channel(channel_id)
    LOGGER.info(f"Checking for updates on channel {channel_id}")


if __name__ == "__main__":
    LOGGER.info("Using config: %s", CONFIG)
    LOGGER.info("Starting execution loop...")
    execution_loop()
