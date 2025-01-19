from fastapi import FastAPI
from app.routes import routes as router

class Server:
    app: FastAPI

    def __init__(self):
        self.app = FastAPI()

    def start(self):
        self.app.include_router(router.router)