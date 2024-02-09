from django.db import models
from common.models import BaseModel

class MonitoringModel(BaseModel):
    spent_time = models.IntegerField()
    max_addon_timing = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    organization_id = models.IntegerField()

    class Meta:
        db_table = 'monitoring'

    def __str__(self) -> str:
        return self.name
    