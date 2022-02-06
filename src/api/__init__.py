from fastapi import FastAPI


APP = FastAPI()


@APP.get("/")
async def root() -> dict:
    return {"message": "Hello World"}
