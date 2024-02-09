import json
import pytest
from rpm_service.models import ConnectivityTypeModel



@pytest.mark.django_db(databases=["rpm_service"])
@pytest.mark.connectivity_type
class TestConnectivityType:
    def test_connectivity_type_model(self):
        ConnectivityTypeModel.objects.create(name="WIFI", description="wifi connectivity")
        connectivity = ConnectivityTypeModel.objects.all()
        
        assert len(connectivity) == 1
    
    
    def test_connectivity_type_list_view(self, client):
        response = client.get("/rpm-service/connectivity-type/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 0
        
        ConnectivityTypeModel.objects.create(name="WIFI", description="wifi connectivity")
        ConnectivityTypeModel.objects.create(name="BLUETOOTH", description="bluetooth connectivity")

        
        response = client.get("/rpm-service/connectivity-type/")
        assert response.status_code == 200
        assert len(response.json()["results"]) == 2
        
        
    
    