from datetime import datetime, timezone


def parse_youtube_datetime(datetime_str: str) -> datetime:
    return datetime.fromisoformat(datetime_str.replace("Z", "+00:00")).astimezone(
        timezone.utc
    )
