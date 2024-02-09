from django.urls import path, include
from rpm_service.routes import router


urlpatterns = [
    path("", include(router.urls), name="rpm_service"),
]
