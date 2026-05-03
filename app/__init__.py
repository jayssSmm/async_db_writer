from fastapi import FastAPI, Request
from app.routers import hobbies
from fastapi.staticfiles import StaticFiles

def create_app():

    app = FastAPI()

    app.include_router(hobbies.router)
    app.mount("/static", StaticFiles(directory="static"), name="static")

    return app
