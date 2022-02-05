from typing import Dict, Type

from config import CONFIG, HistoryProvider
from history.base import BaseHistory
from history.json import JsonHistory


_HISTORY_PROVIDER_MAP: Dict[HistoryProvider, Type[BaseHistory]] = {
    HistoryProvider.JSON: JsonHistory,
}


def get_history_from_config() -> BaseHistory:
    return get_history(CONFIG.history_provider)


def get_history(provider: HistoryProvider) -> BaseHistory:
    return _HISTORY_PROVIDER_MAP[provider]()