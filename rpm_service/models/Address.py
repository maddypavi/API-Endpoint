from django.db import models
from common.models import BaseModel


class AddressModel(BaseModel):
    street = models.CharField(max_length=100, null=True)
    area = models.CharField(max_length=100, null=True)
    city = models.IntegerField()
    pincode = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'address'
    
    def __str__(self):
        return self.city

