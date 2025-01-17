import pytest
from botocore.exceptions import ClientError
from fastapi.testclient import TestClient

from app.Server import Server
from app.cloud_services.aws_service import AwsService
from app.cloud_services.gcp_service import GcpService
from app.exceptions.object_alread_exist_exception import ObjectAlreadyExistException
from unittest.mock import patch, MagicMock

class TestLoad:

    @pytest.fixture
    @patch("app.cloud_services.aws_service.boto3.client")
    def client_init(self, mock_storage):
        mock_s3_client = MagicMock()
        mock_storage.return_value = mock_s3_client
        server = Server(AwsService("access_key", "your_secret_key", "bucket_name", "switzerland", "destination"))
        server.start()
        client = TestClient(server._app)

        return client, mock_s3_client

    def test_load_json_success(self, client_init):
        # Given
        client, mock_s3_client = client_init

        json = {
            "id": 1,
            "name": "Alice",
            "age": 25
        }
        # When
        client.post("/load", json=json)
        # Then
        mock_s3_client.put_object.assert_called_once()


    def test_document_already_exists(self, client_init):
        # Given
        client, mock_s3_client = client_init

        json = {
            "id": 1,
            "name": "Alice",
            "age": 25
        }

        mock_s3_client.put_object.side_effect = ClientError({
            'Error': {
                'Code': 'PreconditionFailed',
                'Message': 'Object already exists!'
            }
        }, "PutObject")

        # When Then
        with pytest.raises(ObjectAlreadyExistException):
            client.post("/load", json=json)