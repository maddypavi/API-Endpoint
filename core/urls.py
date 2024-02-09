from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="OneCare",
        default_version="v2",
        description="OneCare - Python Backend (REST API)",
        terms_of_service="https://onecare.co/terms_of_service",
        contact=openapi.Contact(email="support@onecare.co"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path("admin/", admin.site.urls),
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "playground/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("doc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("", include("index.urls")),
    path("dummy/", include("dummy.urls")),
    path("pytest-report/", include("test_report.urls")),
    path("common/", include("common.urls")),
    path("rpm-service/", include("rpm_service.urls")),
]
