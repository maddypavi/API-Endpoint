from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel, EnumModel


class RequestMonitoringStatusModel(BaseModel):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    status = models.ForeignKey(EnumModel, on_delete=models.CASCADE)
    comments = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'request_monitoring_status'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.status.name}"