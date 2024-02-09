import json
import pytest
from rpm_service.models import AlertTypeModel


@pytest.mark.django_db(databases=["rpm_service"])
@pytest.mark.alert_type
class TestAlertType:
    def test_alert_type_model(self):
        alert = AlertTypeModel.objects.create(
            name="test_alert_type", code="tat", description="test_alert_type"
        )

        assert alert.id is not None
        assert alert.name == "test_alert_type"
        assert alert.code == "tat"
        assert alert.description == "test_alert_type"

    def test_alert_type_list_create_view(self, client):
        response = client.get("/rpm-service/alert-type/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 0

        data = {
            "name": "test_alert_type",
            "code": "tat",
            "description": "test_alert_type",
        }
        response = client.post("/rpm-service/alert-type/", data=data)
        assert response.status_code == 201
        assert response.json()["name"] == "test_alert_type"
        assert response.json()["code"] == "tat"
        assert response.json()["description"] == "test_alert_type"

        response = client.get("/rpm-service/alert-type/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 1

    def test_alert_type_detail_view(self, client):
        data = {
            "name": "test_alert_type",
            "code": "tat",
            "description": "test_alert_type",
        }
        response = client.post("/rpm-service/alert-type/", data=data)
        assert response.status_code == 201
        assert response.json()["name"] == "test_alert_type"
        assert response.json()["code"] == "tat"
        assert response.json()["description"] == "test_alert_type"

        response = client.get("/rpm-service/alert-type/1/")
        assert response.status_code == 200
        assert response.json()["name"] == "test_alert_type"
        assert response.json()["code"] == "tat"
        assert response.json()["description"] == "test_alert_type"

    def test_alert_type_update_view(self, client):
        headers = {"accept": "application/json", "Content-Type": "application/json"}

        data = {
            "name": "test_alert_type",
            "code": "tat",
            "description": "test_alert_type",
        }
        response = client.post("/rpm-service/alert-type/", data=data)
        assert response.status_code == 201
        assert response.json()["name"] == "test_alert_type"
        assert response.json()["code"] == "tat"
        assert response.json()["description"] == "test_alert_type"

        data = {"code": "updated tat"}
        response = client.patch(
            "/rpm-service/alert-type/1/", data=json.dumps(data), headers=headers
        )
        assert response.status_code == 200
        assert response.json()["code"] == "updated tat"

    def test_alert_type_delete_view(self, client):
        headers = {"accept": "application/json", "Content-Type": "application/json"}

        data = {
            "name": "test_alert_type",
            "code": "tat",
            "description": "test_alert_type",
        }
        response = client.post("/rpm-service/alert-type/", data=data)
        assert response.status_code == 201
        assert response.json()["name"] == "test_alert_type"
        assert response.json()["code"] == "tat"
        assert response.json()["description"] == "test_alert_type"

        response = client.delete("/rpm-service/alert-type/1/", headers=headers)
        assert response.status_code == 204

        response = client.get("/rpm-service/alert-type/1/")
        assert response.status_code == 404
