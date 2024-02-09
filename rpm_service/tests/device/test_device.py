import json
import pytest
from rpm_service.models import DeviceModel, ConnectivityTypeModel, DeviceProviderModel


@pytest.mark.django_db(databases=["rpm_service"])
@pytest.mark.device
class TestDevice:
    def test_device_model(self):
        provider = DeviceProviderModel.objects.create(name="test_provider")
        connectivity = ConnectivityTypeModel.objects.create(name="WIFI", description="wifi connectivity")
        device = DeviceModel.objects.create(
            name="test_device", 
            type="sensor", 
            description="test device", 
            connectivity_type=connectivity,
            device_provider=provider
        )
        
        assert device.id is not None
        assert device.name == "test_device" 
        assert device.type == "sensor"
        assert device.description == "test device"
    
    
    def test_device_list_create_view(self, client):
        headers = {"accept": "application/json", "Content-Type": "application/json"}
        provider = DeviceProviderModel.objects.create(name="test_provider")
        connectivity = ConnectivityTypeModel.objects.create(name="WIFI", description="wifi connectivity")
        
        response = client.get("/rpm-service/device/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 0
        
        data = {
            "name": "test_device", 
            "type": "sensor", 
            "description": "test device",
            "connectivity_type": connectivity.id,
            "device_provider": provider.id
        }
        response = client.post("/rpm-service/device/", data=json.dumps(data), headers=headers)
        print(response.json())
        assert response.status_code == 201
        assert response.json()["name"] == "test_device"
        assert response.json()["type"] == "sensor" 
        assert response.json()["description"] == "test device"
        
        response = client.get("/rpm-service/device/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 1
    
    
    # def test_device_detail_view(self, client):
    #     data = {"name": "test_device", "type": "sensor", "description": "test device"}
    #     response = client.post("/rpm-service/device/", data=data)
    #     assert response.status_code == 201
    #     assert response.json()["name"] == "test_device"
    #     assert response.json()["type"] == "sensor"
    #     assert response.json()["description"] == "test device"

    #     response = client.get("/rpm-service/device/1/")
    #     assert response.status_code == 200
    #     assert response.json()["name"] == "test_device"
    #     assert response.json()["type"] == "sensor"
    #     assert response.json()["description"] == "test device"
    
    
    # def test_device_update_view(self, client):
    #     headers = {
    #         "accept": "application/json",
    #         "Content-Type": "application/json"
    #     }
        
    #     data = {"name": "test_device", "type": "sensor", "description": "test device"}
    #     response = client.post("/rpm-service/device/", data=data)
    #     assert response.status_code == 201
    #     assert response.json()["name"] == "test_device"
    #     assert response.json()["type"] == "sensor"
    #     assert response.json()["description"] == "test device"
        
        
    #     data = {"type": "updated sensor"}
    #     response = client.patch("/rpm-service/device/1/", data=json.dumps(data), headers=headers)
    #     assert response.status_code == 200
    #     assert response.json()["type"] == "updated sensor"
        
    
    # def test_device_delete_view(self, client):
    #     headers = {
    #         "accept": "application/json",
    #         "Content-Type": "application/json"
    #     }

    #     data = {"name": "test_device", "type": "sensor", "description": "test device"}
    #     response = client.post("/rpm-service/device/", data=data)
    #     assert response.status_code == 201
    #     assert response.json()["name"] == "test_device"
    #     assert response.json()["type"] == "sensor"
    #     assert response.json()["description"] == "test device"

    #     response = client.delete("/rpm-service/device/1/", headers=headers)
    #     assert response.status_code == 204

    #     response = client.get("/rpm-service/device/1/")
    #     assert response.status_code == 404

