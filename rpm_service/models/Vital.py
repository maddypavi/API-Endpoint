from django.db import models
from common.models import BaseModel

from rpm_service.models import EnumModel

class VitalModel(BaseModel):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    dual_value = models.BooleanField(default=False)
    normal_range_up = models.FloatField()
    normal_range_down = models.FloatField()
    vital_type = models.ForeignKey(EnumModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'vital'

    def __str__(self) -> str:
        return self.name