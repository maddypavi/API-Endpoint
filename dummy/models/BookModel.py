from django.db import models
from django.urls import reverse
from common.models import BaseModel
from dummy.models import Author


class Book(BaseModel):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    pages = models.IntegerField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
