import logging
from datetime import datetime, timezone

from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from history.base import BaseHistory
from models import Channel, Video
from utilities.sqlite import ENGINE, utc_aware


LOGGER = logging.getLogger(__name__)


class SqliteHistory(BaseHistory):
    def __init__(self) -> None:
        self._connection = ENGINE.connect()
        self.Session = sessionmaker(bind=self._connection, expire_on_commit=False)

    def ensure_channel_exists(self, channel_id: str) -> None:
        with self.Session.begin() as session:  # type: ignore
            if session.query(Channel).filter_by(channel_id=channel_id).count() > 0:
                return
            LOGGER.info(f"Channel {channel_id} not found in database, adding it")
            first_seen = datetime.now(timezone.utc)
            channel = Channel(channel_id=channel_id, first_seen=first_seen)
            session.add(channel)

    def video_before_channel_first_seen(
        self, channel_id: str, video_published_at: datetime
    ) -> bool:
        try:
            with self.Session.begin() as session:  # type: ignore
                channel = session.query(Channel).filter_by(channel_id=channel_id).one()
        except NoResultFound:
            LOGGER.warning(f"Channel {channel_id} unexpectedly not found in database")
            return False
        return video_published_at < utc_aware(channel.first_seen)

    def video_already_seen(self, channel_id: str, video_id: str) -> bool:
        del channel_id
        with self.Session.begin() as session:  # type: ignore
            return session.query(Video).filter_by(video_id=video_id).count() > 0

    def mark_video_notified(self, channel_id: str, video_id: str) -> None:
        self.ensure_channel_exists(channel_id)
        if self.video_already_seen(channel_id, video_id):
            return
        notification_sent = datetime.now(timezone.utc)
        video = Video(
            video_id=video_id,
            notification_sent=notification_sent,
            channel_id=channel_id,
        )
        with self.Session.begin() as session:  # type: ignore
            session.add(video)
