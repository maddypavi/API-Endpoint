from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceModel, RPMRequestModel


class DeviceImeiModel(BaseModel):
    imei = models.CharField(max_length=100)
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    owned_by = models.ForeignKey(RPMRequestModel, on_delete=models.SET_NULL, blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'device_imei'

    def __str__(self) -> str:
        return self.device.name