import json
import logging
from io import TextIOWrapper

from config import CONFIG

HISTORY_FILE = "/data/history.json"
LOGGER = logging.getLogger(__name__)


def check_history(channel_id: str, video_id: str) -> bool:
    history = read_history_safe()
    return video_id in history.get(channel_id, [])


def add_to_history(channel_id: str, video_id: str) -> None:
    history = read_history_safe()
    history[channel_id] = history.get(channel_id, [])
    if video_id in history[channel_id]:
        return
    history[channel_id].insert(0, video_id)
    history[channel_id] = history[channel_id][: CONFIG.max_history_per_channel]
    with open(HISTORY_FILE, "w") as history_file:
        history_file.seek(0)
        json.dump(history, history_file)


def read_history_safe() -> dict:
    try:
        with open(HISTORY_FILE, "r") as history_file:
            return json_load_safe(history_file)
    except FileNotFoundError:
        return {}


def json_load_safe(history_file: TextIOWrapper) -> dict:
    try:
        return json.loads(history_file.read())
    except json.JSONDecodeError as err:
        return {}
