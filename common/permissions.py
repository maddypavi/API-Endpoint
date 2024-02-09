from rest_framework.permissions import BasePermission
from django.conf import settings


def setup_testing_environment(permission):
    if settings.DEBUG:
        return True
    return permission


class AuthenticatedUsers(BasePermission):
    def has_permission(self, request, view):
        return setup_testing_environment(request.user_data is not None)

    def has_object_permission(self, request, view, obj):
        return setup_testing_environment(request.user_data is not None)


class ProviderAdminPermissions(BasePermission):
    def has_permission(self, request, view):
        True

    def has_object_permission(self, request, view, obj):
        True


class ProviderPermissions(BasePermission):
    def has_permission(self, request, view):
        True

    def has_object_permission(self, request, view, obj):
        True


class DoctorPermissions(BasePermission):
    def has_permission(self, request, view):
        True

    def has_object_permission(self, request, view, obj):
        True


class PatientPermissions(BasePermission):
    def has_permission(self, request, view):
        True

    def has_object_permission(self, request, view, obj):
        True
