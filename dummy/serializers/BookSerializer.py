from rest_framework import serializers
from common.serializers import BaseSerializer
from dummy.models import Book


class BookSerializer(BaseSerializer):
    author_name = serializers.CharField(source="author.name", read_only=True)

    class Meta:
        model = Book
        fields = BaseSerializer.Meta.fields + [
            "id",
            "title",
            "price",
            "pages",
            "author",
            "author_name",
        ]
