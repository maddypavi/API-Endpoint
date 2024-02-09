from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel, PackageModel

class RequestPackageModel(BaseModel):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    package = models.ForeignKey(PackageModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'request_package'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.package.name}"