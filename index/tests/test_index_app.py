import pytest
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from index.forms import CustomPasswordResetForm, CustomSetPasswordForm


class TestIndexApp:
    def test_homepage(self, client, authenticated_client):
        response = client.get("/")
        assert response.status_code == 302

        response = authenticated_client.get("/")
        assert response.status_code == 200

    def test_user_login_view(self, client, user):
        login_url = reverse("login")
        response = client.get(login_url)
        assert response.status_code == 200

        data = {"username": "user", "password": "password"}
        response = client.post(login_url, data)
        assert response.status_code == 302
        assert response.url == reverse("home")

        data = {"username": "testuser", "password": "wrongpassword"}
        response = client.post(login_url, data)
        assert response.status_code == 200
        assert b"Invalid username or password." in response.content

        response = client.post(login_url, {})
        assert response.status_code == 200
        assert b"This field is required." in response.content

    def test_user_logout_view(self, authenticated_client):
        logout_url = reverse("logout")
        response = authenticated_client.get(logout_url)
        assert response.status_code == 302
        assert response.url == reverse("home")

    def test_custom_password_reset_form_view(self, client):
        password_reset_url = reverse("password_reset")
        response = client.get(password_reset_url)
        assert response.status_code == 200

        data = {"email": "testuser@example.com"}
        response = client.post(password_reset_url, data)
        assert response.status_code == 302
        assert response.url == reverse("password_reset_done")
