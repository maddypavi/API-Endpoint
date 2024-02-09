from django.apps import AppConfig


class RpmServiceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'rpm_service'
    verbose_name = name.replace('_', ' ').title()
