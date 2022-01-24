import logging
from time import sleep


LOGGING_FORMAT = "[%(levelname)s] [%(filename)s:%(lineno)d] <%(funcName)s> %(message)s"
logging.basicConfig(format=LOGGING_FORMAT, level=logging.DEBUG)
LOGGER = logging.getLogger(__name__)


def execution_loop():
    while True:
        LOGGER.info("Hello World!2")
        sleep(1)


if __name__ == "__main__":
    LOGGER.info("Starting execution loop")
    execution_loop()
