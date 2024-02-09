from django.db import models
from common.models import BaseModel

class DeviceProviderModel(BaseModel):
    name = models.CharField(max_length=100)
    enabled = models.BooleanField(default=True)

    class Meta:
        db_table = 'device_provider'

    def __str__(self) -> str:
        return self.name