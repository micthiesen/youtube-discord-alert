import json
import logging
from datetime import datetime, timezone
from typing import TextIO

from config import CONFIG
from history.base import BaseHistory


HISTORY_FILE = "/data/history.json"
LOGGER = logging.getLogger(__name__)


class JsonHistory(BaseHistory):
    def __init__(self):
        self._history = read_history_safe()

    def ensure_channel_exists(self, channel_id: str) -> None:
        changes = False
        if channel_id not in self._history:
            LOGGER.info(f"Channel {channel_id} not in history, adding it")
            self._history[channel_id] = {}
            changes = True
        if "added" not in self._history[channel_id]:
            LOGGER.info(f"Channel {channel_id} added time not set, setting it")
            self._history[channel_id]["added"] = datetime.now(timezone.utc).isoformat()
            changes = True
        if "seen" not in self._history[channel_id]:
            LOGGER.info(f"Channel {channel_id} has no seen list, adding it")
            self._history[channel_id]["seen"] = []
            changes = True

        if changes:
            write_history(self._history)

    def video_before_channel_first_seen(
        self, channel_id: str, video_published_at_str: str
    ) -> bool:
        try:
            added_str = self._history[channel_id]["added"]
        except KeyError:
            return False
        added = datetime.fromisoformat(added_str)
        video_published_at = datetime.fromisoformat(
            video_published_at_str.replace("Z", "+00:00")
        )
        return video_published_at < added

    def video_already_seen(self, channel_id: str, video_id: str) -> bool:
        return video_id in self._history.get(channel_id, {}).get("seen", [])

    def mark_video_seen(self, channel_id: str, video_id: str) -> None:
        self.ensure_channel_exists(channel_id)
        changes = False
        if video_id not in self._history[channel_id]["seen"]:
            self._history[channel_id]["seen"].insert(0, video_id)
            self._history[channel_id]["seen"] = self._history[channel_id]["seen"][
                : CONFIG.max_history_per_channel
            ]
            changes = True

        if changes:
            write_history(self._history)


def write_history(history: dict) -> None:
    with open(HISTORY_FILE, "w") as history_file:
        history_file.seek(0)
        json.dump(history, history_file)


def read_history_safe() -> dict:
    try:
        with open(HISTORY_FILE, "r") as history_file:
            return json_load_safe(history_file)
    except FileNotFoundError:
        return {}


def json_load_safe(history_file: TextIO) -> dict:
    try:
        return json.loads(history_file.read())
    except json.JSONDecodeError:
        return {}
