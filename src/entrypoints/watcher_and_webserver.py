import logging
from threading import Thread

from .watcher import entrypoint as watcher_entrypoint
from .webserver import entrypoint as webserver_entrypoint


LOGGER = logging.getLogger(__name__)


def entrypoint() -> None:
    thread = Thread(target=watcher_entrypoint)
    thread.start()
    webserver_entrypoint()
    thread.join()
