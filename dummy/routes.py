from rest_framework.routers import DefaultRouter
from dummy.views import BookViewSet, AuthorViewSet

router = DefaultRouter()
router.register(r"books", BookViewSet)
router.register(r"authors", AuthorViewSet)
