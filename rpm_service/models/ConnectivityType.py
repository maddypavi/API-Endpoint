from django.db import models
from common.models import BaseModel

class ConnectivityTypeModel(BaseModel):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'connectivity_type'

    def __str__(self):
        return self.name