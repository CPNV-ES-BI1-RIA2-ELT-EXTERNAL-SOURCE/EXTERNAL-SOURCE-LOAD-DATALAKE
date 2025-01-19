from src.cloud_services.cloud_service import CloudService
from google.cloud import storage

class GcpService(CloudService):

    _connection_str : str
    _destination_name : str

    def __init__(self, connection_str : str, destination_name : str):
        pass

    def connect(self) -> None:
        pass

    def disconnect(self) -> None:
        pass

    def load(self, source :any) -> None:
        pass