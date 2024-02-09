from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel

class RequestResponseModel(BaseModel):
    class Status(models.TextChoices):
        APPROVED = "APPROVED"
        CANCELLED = "CANCELLED"
        PENDING = "PENDING"
        
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    request_status = models.CharField(max_length=20, choices=Status)

    class Meta:
        db_table = 'request_response'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.request_status}"