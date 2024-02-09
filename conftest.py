import pytest
from django.test import Client
from django.conf import settings
from django.contrib.auth.models import User


@pytest.fixture(scope="session")
def django_db_setup(django_db_setup, django_db_blocker):
    """
    This fixture ensures that Django creates a test database and reuses it
    for the duration of the test session.
    """
    with django_db_blocker.unblock():
        User.objects.create_superuser("admin", "admin@admin.com", "password")
    settings.DEBUG = True
    yield


def pytest_addoption(parser):
    parser.addoption(
        "--databases",
        action="append",
        default=["default"],
        help="List of database aliases to include in tests.",
    )


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db, request):
    # Get the specified databases from the command line option
    databases_option = request.config.getoption("--databases")


@pytest.fixture
def authenticated_client(db):
    user = User.objects.create_user(username="user", password="password")
    client = Client()
    client.login(username="user", password="password")
    return client


@pytest.fixture
def user(db):
    return User.objects.create_user(username="user", password="password")


@pytest.fixture
def client(db):
    """
    This fixture provides a Django test client for use in your tests.
    """
    return Client()
