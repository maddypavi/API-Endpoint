from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceProviderModel, ConnectivityTypeModel

class DeviceModel(BaseModel):
    external_id = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    feature_description = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    manufactured_by = models.CharField(max_length=100)
    connectivity_type = models.ForeignKey(ConnectivityTypeModel, on_delete=models.CASCADE)
    device_provider = models.ForeignKey(DeviceProviderModel, on_delete=models.CASCADE)
    uuid = models.CharField(max_length=255, blank=True, null=True)
    organization_id = models.IntegerField(blank=True, null=True)
    rental_cost = models.FloatField(blank=True, null=True)
    buy_cost = models.FloatField(blank=True, null=True)
    image_url = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'device'

    def __str__(self) -> str:
        return self.name
