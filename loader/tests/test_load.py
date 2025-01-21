# récupération du document avec un url fictif
# load dans un faux micros service mocké
# test cas d'erreurs
# retourner lien ou erreur

import json
import pytest

from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.exceptions.environement_varriables_exception import EnvironmentVariableException
from app.Server import Server
from app.exceptions.object_alread_exist_exception import ObjectAlreadyExistException
from unittest.mock import patch, MagicMock

class TestLoad:
    _JSON_FILE_PATH = "../stationboard-Lausanne-01.12.2024-00.01-ALL.json"
    _OBJECT_URL = "http://fake-url.com"

    @pytest.fixture
    def client_init(self):
        server = Server()
        server.start()
        client = TestClient(server.app)
        return client

    @patch("app.services.api_service")
    def test_load_json_success(self, client_init):
        # Given
        client = client_init

        params = {
            "url": self._OBJECT_URL,
        }

        with open(self._JSON_FILE_PATH, "rb") as file:
            files = {"object": (self._JSON_FILE_PATH.split("/")[-1], file, "application/json")}

            mock_s3_client = MagicMock()
            mock_api_service.side_effect = [
                {"data": file},
                {"data": self._OBJECT_URL}
            ]

            # When
            response = client.post("/v1/raw-object", params=params)

            # Then
            assert response.status_code == 200