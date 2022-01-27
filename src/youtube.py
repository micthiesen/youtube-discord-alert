from typing import List

from pyyoutube import Api, PlaylistItem

from config import CONFIG


API = Api(api_key=CONFIG.youtube_api_key)


class YoutubeError(Exception):
    pass


def get_latest_channel_videos(
    channel_id: str, count: int = CONFIG.latest_channel_videos_count
) -> List[PlaylistItem]:
    channel_list_response = API.get_channel_info(channel_id=channel_id)
    try:
        channel = channel_list_response.items[0]
    except IndexError:
        raise YoutubeError(f"Channel {channel_id} does not exist")
    uploads_playlist = channel.contentDetails.relatedPlaylists.uploads
    playlist_item_response = API.get_playlist_items(
        playlist_id=uploads_playlist, count=count
    )
    return list(reversed(playlist_item_response.items))
