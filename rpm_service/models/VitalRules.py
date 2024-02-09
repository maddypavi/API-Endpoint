from django.db import models
from common.models import BaseModel

from rpm_service.models import VitalModel, RPMRequestModel, EnumModel

class VitalRulesModel(BaseModel):
    vital = models.ForeignKey(VitalModel, on_delete=models.CASCADE)
    request = models.ForeignKey(RPMRequestModel, on_delete=models.SET_NULL, null=True)
    timing_periods = models.IntegerField(null=True)
    day_periods = models.IntegerField(null=True)
    taken_state = models.ForeignKey(EnumModel, on_delete=models.SET_NULL, null=True)
    taken_state_mins = models.IntegerField(null=True)
    exact_time = models.TimeField(null=True)

    class Meta:
        db_table = 'vital_rules'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.vital.name}"