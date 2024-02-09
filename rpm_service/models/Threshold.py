from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel, AlertTypeModel, VitalModel, EnumModel

class ThresholdModel(BaseModel):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.SET_NULL, null=True)
    alert_type = models.ForeignKey(AlertTypeModel, on_delete=models.CASCADE)
    vital = models.ForeignKey(VitalModel, on_delete=models.CASCADE)
    taken_state = models.ForeignKey(EnumModel, on_delete=models.SET_NULL, null=True, related_name="threshold_taken_state")
    relation = models.ForeignKey(EnumModel, on_delete=models.CASCADE, related_name="threshold_relation")
    value1 = models.FloatField()
    value2 = models.FloatField(null=True)
    level = models.ForeignKey(EnumModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'threshold'
    
    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.alert_type.name} - {self.vital.name}"
