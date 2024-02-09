from django.core.management.base import BaseCommand
from django.db import transaction
from rpm_service.models import AlertTypeModel

class Command(BaseCommand):
    help = 'Seed data for AlertType model'

    @transaction.atomic
    def handle(self, *args, **options):
        alert_types_data = [
            {'code': 'RED', 'name': 'Red', 'description': 'Danger', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'code': 'ORANGE', 'name': 'Orange', 'description': 'Warning', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'code': 'GREEN', 'name': 'Green', 'description': 'Normal', 'status': True, 'created_at': 'now()', 'created_by': 1},
        ]

        for alert_type_data in alert_types_data:
            AlertTypeModel.objects.create(**alert_type_data)
            self.stdout.write(self.style.SUCCESS(f'AlertType {alert_type_data["name"]} created successfully.'))

        self.stdout.write(self.style.SUCCESS('AlertType data seeded successfully.'))
