import logging

from entrypoints import get_entrypoint_from_config
from utilities.config import CONFIG


LOGGER = logging.getLogger(__name__)
LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"


if __name__ == "__main__":
    logging.basicConfig(format=LOGGING_FORMAT, level=CONFIG.log_level_parsed)
    LOGGER.info("Using config:\n%s", CONFIG.to_string(" ---> "))
    get_entrypoint_from_config()()
