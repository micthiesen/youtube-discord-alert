from typing import Dict, Type

from history.base import BaseHistory
from history.json import JsonHistory
from history.sqlite import SqliteHistory
from utilities.config import CONFIG, HistoryProvider


_HISTORY_PROVIDER_MAP: Dict[HistoryProvider, Type[BaseHistory]] = {
    HistoryProvider.JSON: JsonHistory,
    HistoryProvider.SQLITE: SqliteHistory,
}


def get_history_from_config() -> BaseHistory:
    return get_history(CONFIG.history_provider)


def get_history(provider: HistoryProvider) -> BaseHistory:
    return _HISTORY_PROVIDER_MAP[provider]()
