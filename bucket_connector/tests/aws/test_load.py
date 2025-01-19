import json
import pytest

from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.exceptions.environement_varriables_exception import EnvironmentVariableException
from app.Server import Server
from app.exceptions.object_alread_exist_exception import ObjectAlreadyExistException
from unittest.mock import patch, MagicMock

class TestLoad:
    _BUCKET_NAME : str= "s3-bucket"
    _BUCKET_DESTINATION : str = "path/to/destination/folder"
    _JSON_FILE_PATH = "../stationboard-Lausanne-01.12.2024-00.01-ALL.json"

    @pytest.fixture
    @patch("app.cloud_services.aws_service.boto3.client")
    def client_init(self, mock_storage):
        try:
            mock_s3_client = MagicMock()
            mock_storage.return_value = mock_s3_client

            server = Server()
            server.start()
            client = TestClient(server.app)

            return client, mock_s3_client
        except EnvironmentVariableException as e:
            print("Error:", e)

    def test_load_json_success(self, client_init):
        # Given
        client, mock_s3_client = client_init
        with open(self._JSON_FILE_PATH, "rb") as file:
            files = {"object": (self._JSON_FILE_PATH.split("/")[-1], file, "application/json")}
            form_data = {
                "bucket_name": self._BUCKET_NAME,
                "bucket_destination": self._BUCKET_DESTINATION,
            }

            # When
            response = client.post("/v1/object", data=form_data, files=files)

            # Then
            assert response.status_code == 200
            # Vérification que put_object a bien été appelé
            mock_s3_client.put_object.assert_called_once_with(
                Bucket=self._BUCKET_NAME,
                Key=self._BUCKET_DESTINATION,
                Body=files["object"][1]  # Vérification que le corps du fichier est correctement passé
            )

    def test_document_already_exists(self, client_init):
        # Given
        client, mock_s3_client = client_init

        mock_s3_client.put_object.side_effect = ClientError({
            'Error': {
                'Code': 'PreconditionFailed',
                'Message': 'Object already exists!'
            }
        }, "PutObject")

        with open(self._JSON_FILE_PATH, "rb") as file:
            files = {"object": (self._JSON_FILE_PATH.split("/")[-1], file, "application/json")}
            form_data = {
                "bucket_name": self._BUCKET_NAME,
                "bucket_destination": self._BUCKET_DESTINATION,
            }


            # When
            client.post("/v1/object", data=form_data, files=files)

            # Then
            with pytest.raises(ObjectAlreadyExistException):
                client.post("/load", json=json)