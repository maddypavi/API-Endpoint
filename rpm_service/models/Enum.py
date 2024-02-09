from django.db import models
from common.models import BaseModel

class EnumModel(BaseModel):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    class Meta:
        db_table = 'enum'

    def __str__(self) -> str:
        return self.name