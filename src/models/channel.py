from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from .base import Base


if TYPE_CHECKING:
    from models import Video  # noqa: F401


class Channel(Base):
    __tablename__ = "channel"
    channel_id = Column(String, primary_key=True)
    first_seen = Column(DateTime, nullable=False)
    videos = relationship("Video", backref="channel")
