import logging
from datetime import datetime, timezone

from fastapi import APIRouter, Form, HTTPException
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

from models import Channel
from services.youtube import YoutubeError, get_channel
from utilities.sqlite import ENGINE


LOGGER = logging.getLogger(__name__)
ROUTER = APIRouter()
Session = sessionmaker(bind=ENGINE.connect(), expire_on_commit=False)


@ROUTER.post("", status_code=201)
async def create_channel(channel_id: str = Form(...)) -> None:
    try:
        get_channel(channel_id=channel_id)
    except YoutubeError as err:
        raise HTTPException(status_code=400, detail=str(err))
    with Session.begin() as session:  # type: ignore
        try:
            channel = session.query(Channel).filter_by(channel_id=channel_id).one()
        except NoResultFound:
            first_seen = datetime.now(timezone.utc)
            channel = Channel(channel_id=channel_id, first_seen=first_seen)
            session.add(channel)
        else:
            if channel.deleted:
                channel.deleted = False
    return None


@ROUTER.delete("/{channel_id}", status_code=204)
async def delete_channel(channel_id: str) -> None:
    return None
