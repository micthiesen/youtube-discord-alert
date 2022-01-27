from typing import List

from pyyoutube import Api, Subscription


API = Api()
PARTS_DEFAULT = "id,snippet"
COUNT_DEFAULT = 10


def get_subscription_by_channel(
    channel_id: str, parts: str = PARTS_DEFAULT, count: int = COUNT_DEFAULT
) -> List[Subscription]:
    return API.get_subscription_by_channel(
        channel_id=channel_id, parts=parts, count=count
    ).items
