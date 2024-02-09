from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceModel, RPMRequestModel, VitalModel


class VitalReadingModel(BaseModel):
    data_id = models.CharField(max_length=255, null=True)
    device = models.ForeignKey(DeviceModel, on_delete=models.SET_NULL, null=True)
    request = models.ForeignKey(RPMRequestModel, on_delete=models.SET_NULL, null=True)  #
    vital = models.ForeignKey(VitalModel, on_delete=models.CASCADE)
    high_value = models.FloatField(null=True)
    low_value = models.FloatField(null=True)
    vital_jsonb_data = models.JSONField(null=True)
    collection_date = models.DateTimeField()

    class Meta:
        db_table = "vital_reading"

    def __str__(self) -> str:
        return f"{self.data_id} - {self.vital.name} - {self.collection_date}"