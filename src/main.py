import logging
from time import sleep

from config import CONFIG


LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def execution_loop():
    while True:
        LOGGER.info("Hello World!")
        sleep(CONFIG.poll_interval)


if __name__ == "__main__":
    LOGGER.info("Using config: %s", CONFIG)
    LOGGER.info("Starting execution loop...")
    execution_loop()
