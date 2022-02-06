import logging

import uvicorn

from api import APP
from utilities.config import CONFIG


LOGGER = logging.getLogger(__name__)


def entrypoint() -> None:
    LOGGER.info(f"Listening at http://localhost:{CONFIG.webserver_port}...")
    uvicorn.run(APP, port=CONFIG.webserver_port, host="0.0.0.0", log_level="warning")
