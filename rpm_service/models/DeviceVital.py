
from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceModel, VitalModel

class DeviceVitalModel(BaseModel):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    vital = models.ForeignKey(VitalModel, on_delete=models.CASCADE)
    high_value_string = models.CharField(max_length=255, null=True)
    low_value_string = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'device_vital'
    
    def __str__(self) -> str:
        return f"{self.device.name} - {self.vital.name}"