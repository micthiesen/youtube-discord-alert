import logging

from entrypoints.watcher import start_watcher
from utilities.config import CONFIG


LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=CONFIG.log_level_parsed)
LOGGER = logging.getLogger(__name__)


if __name__ == "__main__":
    LOGGER.info("Using config: %s", CONFIG)
    start_watcher()
