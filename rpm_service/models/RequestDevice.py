from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel, DeviceModel, DeviceImeiModel

class RequestDeviceModel(BaseModel):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    device_imei = models.ForeignKey(DeviceImeiModel, on_delete=models.CASCADE, null=True)
    rent = models.BooleanField(null=True)
    existing = models.BooleanField(null=True)

    class Meta:
        db_table = 'request_device'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.device.name}"