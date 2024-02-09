from django_filters import FilterSet
from django_filters.rest_framework import filters
from dummy.models import Book


class BookFilter(FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    pages = filters.NumberFilter(field_name="pages", lookup_expr="gte")
    author = filters.CharFilter(field_name="author__name", lookup_expr="icontains")

    class Meta:
        model = Book
        fields = ["title", "pages", "author"]
