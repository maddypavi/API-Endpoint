from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from test_report.utils import pytest_coverage_report, pytest_test_report


@login_required(login_url="/login/")
def pytest_report(request):
    coverage, grade = pytest_coverage_report()
    report, created = pytest_test_report()
    context = {
        "report": report,
        "coverage": coverage,
        "grade": grade,
        "created": created,
    }
    return render(request, "pytest_report.html", context)
