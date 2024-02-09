from django.db import models
from common.models import BaseModel

class AlertTypeModel(BaseModel):
    code = models.CharField(max_length=100, null=False)
    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=200, null=False)
    
    class Meta:
        db_table = 'alert_types'
    
    def __str__(self):
        return self.name
