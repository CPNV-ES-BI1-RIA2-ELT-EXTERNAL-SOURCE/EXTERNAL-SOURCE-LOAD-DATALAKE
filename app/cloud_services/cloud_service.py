from pydantic import json

from app.objects.object import Object


class CloudService:
    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def load(self, source : any) -> None:
        pass