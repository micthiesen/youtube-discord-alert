from fastapi import APIRouter, FastAPI
from fastapi.staticfiles import StaticFiles

from . import channels


APP = FastAPI()
APP.mount("/", StaticFiles(directory="/www", html=True), name="static")

API = APIRouter()
API.include_router(channels.ROUTER, prefix="/channels")

APP.include_router(API, prefix="/api")
