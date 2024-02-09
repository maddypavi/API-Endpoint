import django_filters as filters
from dummy.models import Author


class AuthorFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr="icontains")
    age = filters.NumberFilter(lookup_expr="exact")

    class Meta:
        model = Author
        fields = ["name", "age"]
