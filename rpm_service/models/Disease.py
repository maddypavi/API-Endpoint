from django.db import models
from common.models import BaseModel

class DiseaseModel(BaseModel):
    external_id = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    organization_id = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'disease'
    
    def __str__(self) -> str:
        return self.name
