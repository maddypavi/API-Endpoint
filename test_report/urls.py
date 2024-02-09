from django.urls import path
from test_report.views import pytest_report

app_name = "test_report"

urlpatterns = [
    path("", pytest_report, name="pytest-report"),
]
