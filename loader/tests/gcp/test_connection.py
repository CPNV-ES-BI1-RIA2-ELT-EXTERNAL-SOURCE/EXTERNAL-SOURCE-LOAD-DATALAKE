import pytest

from src.Server import Server
from src.cloud_services.gcp_service import GcpService
from src.exceptions.authentication_failed_exception import AuthenticationFailedException
from src.exceptions.destination_not_found_exception import DestinationNotFoundException
from unittest.mock import patch, MagicMock

class TestConnection:

    @patch("src.cloud_services.gcp_service.storage")
    def test_cannot_connect_to_datalake_authentication_failed(self, mock_storage):
        # Given
        server = Server("localhost", 8000)
        wrong_connection_string = "invalid_connection_string"  # Chaîne de connexion incorrecte
        destination_name = "bucket"
        server.start(GcpService(wrong_connection_string, destination_name))
        json_file = "data/file.json"

        mock_client = MagicMock()
        mock_storage.Client.from_service_account_json.return_value = mock_client
        mock_client.from_service_account_json.side_effect = AuthenticationFailedException("Authentication failed")

        # When
        #Then
        with pytest.raises(AuthenticationFailedException):
            server.load(json_file)

    @patch("src.cloud_services.gcp_service.storage")
    def test_cannot_connect_to_datalake_not_found(self, mock_storage):
        # Given
        server = Server("localhost", 8000)
        connection_string = "valid_connection_string"
        wrong_destination_name = "wrong_bucket"
        json_file = "data/file.json"
        server.start(GcpService(connection_string, wrong_destination_name))

        mock_client = MagicMock()
        mock_storage.Client.from_service_account_json.return_value = mock_client
        mock_bucket = MagicMock()
        mock_client.bucket.return_value = mock_bucket
        mock_bucket.exists.return_value = False

        # When:
        with pytest.raises(DestinationNotFoundException):
            server.load(json_file)

        mock_client.bucket.assert_called_once_with(wrong_destination_name)
        mock_bucket.exists.assert_called_once()