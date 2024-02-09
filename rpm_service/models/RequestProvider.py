from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel

class RequestProviderModel(models.Model):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    provider_id = models.IntegerField()
    primary = models.BooleanField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    provider_first_name = models.CharField(max_length=100, null=True)
    provider_last_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'request_provider'
    
    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.provider_id}"
