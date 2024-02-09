from django.db import models
from common.models import BaseModel

from rpm_service.models import DeviceModel, RequestResponseModel


class ResponseDeviceModel(BaseModel):
    device = models.ForeignKey(DeviceModel, on_delete=models.CASCADE)
    request_response = models.ForeignKey(RequestResponseModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'response_device'

    def __str__(self) -> str:
        return f"{self.device.name} - {self.request_response.request.external_id}"