from sqlalchemy import Column, DateTime, ForeignKey, String

from .base import Base


class Video(Base):
    __tablename__ = "video"
    video_id = Column(String, primary_key=True)
    notification_sent = Column(DateTime, nullable=False)
    channel_id = Column(String, ForeignKey("channel.channel_id"), nullable=False)
