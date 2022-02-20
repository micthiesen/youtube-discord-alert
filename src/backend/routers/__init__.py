from fastapi import FastAPI

from . import channels


APP = FastAPI()
APP.include_router(channels.ROUTER, prefix="/channels")
