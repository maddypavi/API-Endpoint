import pytest
from test_report.utils import (
    parse_datetime,
    format_keys,
    pytest_coverage_report,
    pytest_test_report,
)


class TestReportApp:
    def test_parse_datetime(self):
        assert parse_datetime("2022-01-01T00:00:00") == "2022-01-01 00:00:00"
        assert parse_datetime(1703574727.7963324) == "2023-12-26 12:42:07"
        assert parse_datetime("some text") is None

    def test_format_keys(self):
        assert format_keys({"test_num": 1}) == {"Test Num": 1}

    def test_pytest_coverage_report(self):
        assert pytest_coverage_report() is not None

    def test_pytest_test_report(self):
        assert pytest_test_report() is not None

    def test_unauthenticated_access_redirects(self, client):
        response = client.get("/pytest-report")
        assert response.status_code == 301

    def test_authenticated_access_succeeds(self, authenticated_client):
        auth_response = authenticated_client.post(
            "/login/", data={"username": "admin", "password": "admin"}
        )
        assert auth_response.status_code == 200

        response = authenticated_client.get("/pytest-report")
        assert response.status_code == 301
