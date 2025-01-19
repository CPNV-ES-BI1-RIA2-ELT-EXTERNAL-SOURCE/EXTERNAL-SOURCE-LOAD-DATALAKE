import pytest

from src.Server import Server
from src.cloud_services.gcp_service import GcpService
from src.exceptions.object_alread_exist_exception import ObjectAlreadyExistException
from unittest.mock import patch, MagicMock


class TestLoad:

    @pytest.fixture
    def setup_server_and_json_file(self):
        server = Server("localhost", 8000)
        connection_string = "fake_connection_string"
        destination_name = "test-bucket"
        json_file = "data/file.json"

        server.start(GcpService(connection_string, destination_name))

        return server, json_file

    @patch("src.cloud_services.gcp_service.storage")
    def test_load_json_success(self, mock_storage, setup_server_and_json_file):
        #Given
        server, json_file = setup_server_and_json_file

        mock_client = MagicMock()
        mock_storage.Client.from_service_account_json.return_value = mock_client
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_blob.exists.return_value = False
        mock_client.bucket.return_value = mock_bucket
        mock_bucket.blob.return_value = mock_blob


        # When:
        server.load(json_file)

        # Then
        mock_client.bucket.assert_called_once_with("test-bucket")
        mock_bucket.blob.assert_called_once_with(json_file)
        mock_blob.upload_from_filename.assert_called_once_with(json_file)

    @patch("src.cloud_services.gcp_service.storage")
    def test_document_already_exists(self, mock_storage, setup_server_and_json_file):
        # Given
        server, json_file = setup_server_and_json_file

        mock_client = MagicMock()
        mock_storage.Client.from_service_account_json.return_value = mock_client
        mock_bucket = MagicMock()
        mock_blob = MagicMock()
        mock_blob.exists.return_value = True
        mock_client.bucket.return_value = mock_bucket
        mock_bucket.blob.return_value = mock_blob

        # When
        # Then
        with pytest.raises(ObjectAlreadyExistException):
            server.load(json_file)