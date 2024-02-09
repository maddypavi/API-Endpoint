from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from dummy.models import Author
from dummy.serializers import AuthorSerializer
from common.utils import Pagination
from dummy.filters import SortFilterBackend
from dummy.filters.AuthorFilter import AuthorFilter


class AuthorViewSet(ModelViewSet):
    """
    API endpoint for managing authors.
    """

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = Pagination
    filterset_class = AuthorFilter
    filter_backends = [OrderingFilter, SortFilterBackend]
    http_method_names = ["get", "post", "retrieve", "patch", "delete"]
    ordering = ["id"]

    