from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceModel

class DeviceAssignmentModel(BaseModel):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    patient_id = models.IntegerField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    assigned_by = models.IntegerField()

    class Meta:
        db_table = 'device_assignment'
    
    def __str__(self) -> str:
        return self.device.name
