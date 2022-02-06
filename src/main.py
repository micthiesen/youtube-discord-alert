import logging

from entrypoints import get_entrypoint_from_config
from utilities.config import CONFIG, HistoryProvider
from utilities.sqlite import initialize_db


LOGGER = logging.getLogger(__name__)
LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"


if __name__ == "__main__":
    logging.basicConfig(format=LOGGING_FORMAT, level=CONFIG.log_level_parsed)
    LOGGER.info("Using config:\n%s", CONFIG.to_string(" ---> "))
    if CONFIG.history_provider == HistoryProvider.SQLITE:
        initialize_db()
    get_entrypoint_from_config()()
