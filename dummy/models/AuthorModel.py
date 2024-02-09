from django.db import models
from django.urls import reverse
from common.models import BaseModel


class Author(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])
