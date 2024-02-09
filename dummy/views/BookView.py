from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from common.utils import Pagination
from common.logging.ntfy import ntfy_notification
from common.exceptions import DuplicateObjectCreationException
from dummy.filters import BookFilter, SortFilterBackend
from dummy.models import Book
from dummy.serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    API endpoint for managing books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination
    filterset_class = BookFilter
    filter_backends = [OrderingFilter, SortFilterBackend]
    http_method_names = ["get", "post", "retrieve", "patch", "delete"]
    ordering = ["id"]

    def get_queryset(self):
        return BookFilter(self.request.GET, queryset=self.queryset).qs

    def create(self, request, *args, **kwargs):
        title = request.data.get("title", None)
        author = request.data.get("author", None)
        book = Book.objects.filter(title=title, author=author).first()

        if book:
            raise DuplicateObjectCreationException
        return super().create(request, *args, **kwargs)
