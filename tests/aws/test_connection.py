import pytest
from botocore.exceptions import ClientError
from botocore.monitoring import MonitorEventAdapter

from app.Server import Server
from app.cloud_services.aws_service import AwsService
from app.cloud_services.gcp_service import GcpService
from app.exceptions.authentication_failed_exception import AuthenticationFailedException
from app.exceptions.destination_not_found_exception import DestinationNotFoundException
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient


class TestConnection:

    @patch("app.cloud_services.aws_service.boto3.client")
    def test_cannot_connect_to_datalake_authentication_failed(self, mock_storage):
        # Given
        mock_storage.side_effect = AuthenticationFailedException("")

        server = Server(AwsService("access_key", "your_secret_key", "bucket_name", "switzerland", "destination"))

        json = [
            {"id": 1, "name": "Alice", "age": 25},
            {"id": 2, "name": "Bob", "age": 30}
        ]

        client = TestClient(server._app)

        # When / Then
        with pytest.raises(AuthenticationFailedException):
            server.start()


    @patch("app.cloud_services.aws_service.boto3.client")
    def test_cannot_connect_to_datalake_not_found(self, mock_storage):
        # Given
        mock_s3_client = MagicMock()
        mock_s3_client.put_object.side_effect = ClientError({
        'Error': {
            'Code': 'NoSuchBucket',
            'Message': 'The specified bucket does not exist'
        }
    }, "PutObject")
        mock_storage.return_value = mock_s3_client

        server = Server(AwsService("access_key", "your_secret_key", "bucket_name", "switzerland", "destination"))
        server.start()
        json = {
          "id": 1,
          "name": "Alice",
          "age": 25
        }

        client = TestClient(server._app)

        # When / Then
        with pytest.raises(DestinationNotFoundException):
            client.post("/load", json=json)
