from typing import List

from pyyoutube import Api, Channel, PlaylistItem

from utilities.config import CONFIG


API = Api(api_key=CONFIG.youtube_api_key)


class YoutubeError(Exception):
    pass


def get_channel(channel_id: str) -> Channel:
    channel_list_response = API.get_channel_info(channel_id=channel_id)
    try:
        return channel_list_response.items[0]
    except (IndexError, TypeError):
        raise YoutubeError(f"Channel {channel_id} does not exist")


def get_latest_channel_videos(
    channel_id: str, count: int = CONFIG.latest_channel_videos_count
) -> List[PlaylistItem]:
    channel = get_channel(channel_id=channel_id)
    uploads_playlist = channel.contentDetails.relatedPlaylists.uploads
    playlist_item_response = API.get_playlist_items(
        playlist_id=uploads_playlist, count=count
    )
    return list(reversed(playlist_item_response.items))
