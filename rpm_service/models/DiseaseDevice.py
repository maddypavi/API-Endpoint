from django.db import models
from common.models import BaseModel

from rpm_service.models import DiseaseModel, DeviceModel

class DiseaseDeviceModel(BaseModel):
    disease = models.ForeignKey(DiseaseModel, on_delete=models.CASCADE)
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
   
    class Meta:
        db_table = 'disease_device'
    
    def __str__(self) -> str:
        return f"{self.disease.name} - {self.device.name}"
