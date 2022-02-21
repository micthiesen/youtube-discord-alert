from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from . import channels


API_APP = FastAPI()
API_APP.include_router(channels.ROUTER, prefix="/channels")

APP = FastAPI()
APP.mount("/api", API_APP)
APP.mount("/", StaticFiles(directory="/www", html=True), name="static")
