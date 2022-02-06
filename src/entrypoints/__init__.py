from typing import Callable, Dict

from entrypoints.watcher import entrypoint as watcher_entrypoint
from utilities.config import CONFIG, Entrypoint


_ENTRYPOINT_MAP: Dict[Entrypoint, Callable[[], None]] = {
    Entrypoint.WATCHER: watcher_entrypoint
}


def get_entrypoint_from_config() -> Callable[[], None]:
    return get_entrypoint(CONFIG.entrypoint)


def get_entrypoint(entrypoint: Entrypoint) -> Callable[[], None]:
    return _ENTRYPOINT_MAP[entrypoint]
