from django.db import models
from common.models import BaseModel

from rpm_service.models import DiseaseModel, AddressModel


class RPMRequestModel(BaseModel):
    external_id = models.CharField(max_length=255)
    patient_id = models.IntegerField()
    organization_id = models.IntegerField()
    provider_id = models.IntegerField(null=True)
    disease = models.ForeignKey(DiseaseModel, on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey(AddressModel, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255, null=True)
    self_monitoring = models.BooleanField(null=True)
    imei = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'rpm_request'
    
    def __str__(self) -> str:
        return f"{self.external_id} - {self.patient_id}"
    
