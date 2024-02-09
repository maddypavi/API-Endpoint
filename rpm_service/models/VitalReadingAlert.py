from django.db import models
from common.models import BaseModel

from rpm_service.models import VitalReadingModel, AlertTypeModel, ThresholdModel

class VitalReadingAlertModel(BaseModel):
    vital_reading = models.ForeignKey(VitalReadingModel, on_delete=models.CASCADE)
    alert_type = models.ForeignKey(AlertTypeModel, on_delete=models.CASCADE)
    threshold = models.ForeignKey(ThresholdModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vital_reading_alert'

    def __str__(self) -> str:
        return f"{self.vital_reading.data_id} - {self.alert_type.name} - {self.threshold.vital.name}"