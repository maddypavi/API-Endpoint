from django.db import models
from common.models import BaseModel

from rpm_service.models import RPMRequestModel

class RPMBillModel(BaseModel):
    request = models.ForeignKey(RPMRequestModel, on_delete=models.CASCADE)
    bill_id = models.IntegerField()
    paid = models.BooleanField(default=False)

    class Meta:
        db_table = 'rpm_bill'

    def __str__(self) -> str:
        return f"{self.request.external_id} - {self.bill_id} - {self.paid}"