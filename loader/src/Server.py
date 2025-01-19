from fastapi import FastAPI, Request

from loader.src.cloud_services.cloud_service import CloudService


class Server:
    app : FastAPI
    _service : CloudService

    def __init__(self, service : CloudService):
        self._service = service
        self.app = FastAPI()

    def start(self):
        self._service.connect()

        @self.app.post("/load")
        async def load_content(request: Request):
            # TODO : implement multy types with object types
            self._service.load(await request.json())


    def stop(self):
        self._service.disconnect()