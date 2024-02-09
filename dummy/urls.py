from django.urls import path, include
from dummy.routes import router


urlpatterns = [
    path("", include(router.urls), name="dummy"),
]
