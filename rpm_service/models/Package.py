from django.db import models
from common.models import BaseModel

from rpm_service.models import MonitoringModel, EnumModel

class PackageModel(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    period = models.IntegerField()
    enrollment_cost = models.FloatField(null=True)
    monitoring_cost = models.FloatField(null=True)
    addon_cost = models.FloatField(null=True)
    discount = models.FloatField(null=True)
    offer = models.FloatField(null=True)
    organization_id = models.IntegerField()
    payment_type = models.ForeignKey(EnumModel, on_delete=models.CASCADE)
    rule_id = models.ForeignKey(MonitoringModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'package'

    def __str__(self) -> str:
        return self.name