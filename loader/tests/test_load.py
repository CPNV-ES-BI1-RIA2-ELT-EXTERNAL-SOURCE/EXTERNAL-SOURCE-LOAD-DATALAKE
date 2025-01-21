import pytest
from fastapi.testclient import TestClient
from app.Server import Server
from unittest.mock import patch, MagicMock
from app.services.api_service import api_service

class TestLoad:
    _JSON_FILE_PATH = "./stationboard-Lausanne-01.12.2024-00.01-ALL.json"
    _OBJECT_URL = "http://fake-url.com"

    @pytest.fixture
    def client_init(self):
        server = Server()
        server.start()
        client = TestClient(server.app)
        return client

    @patch("app.services.api_service")
    def test_load_json_success(self, mock_api_service, client_init):
        # Given
        client = client_init

        params = {
            "dataDestination": "s3://my-bucket-name/folder/data-file.csv",
            "dataSource": self._OBJECT_URL,
        }

        with open(self._JSON_FILE_PATH, "rb") as file_obj:
            files = {"object": (self._JSON_FILE_PATH.split("/")[-1], file_obj, "application/json")}

            # Mock le service API
            mock_api_service.side_effect = [
                {"data": {"mocked": "file_content"}},
                {"data": self._OBJECT_URL}
            ]

            # When
            response = client.post("/v1/raw-object", data=params, files=files)

            # Then
            assert response.status_code == 200
