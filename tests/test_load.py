from unittest.mock import patch, MagicMock

import pytest
from fastapi.testclient import TestClient
from app.main import app

class TestJobRoute:
    @pytest.fixture
    def client_init(self):
        return TestClient(app)

    @patch("app.services.api_service.api_service")
    def test_job_route_success(self, mock_api_service, client_init):
        # Given
        client = client_init
        job_id = 123
        payload = {
            "dataSource": "http://mock-data-source.com",
            "dataDestination": "s3://mock-destination-bucket/file.csv",
        }

        # Mock responses for `api_service`
        mock_response = MagicMock()
        mock_response.return_value = "prot"
        mock_api_service.return_value = mock_response

        # When
        # TODO update route
        response = client.post(f"/job/{job_id}", json=payload)

        # Then
        # TODO remove printf instruction
        print(f"Response JSON: {response.json()}")
        assert response.status_code == 200
        assert response.json() == {"data": "mocked_loader_response"}
