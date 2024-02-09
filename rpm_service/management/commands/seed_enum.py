from django.core.management.base import BaseCommand
from django.db import transaction
from rpm_service.models import EnumModel

class Command(BaseCommand):
    help = 'Seed data for Enum model'

    @transaction.atomic
    def handle(self, *args, **options):
        enum_data = [
            {'name': 'Prepaid', 'type': 'PAYMENT_TYPE', 'code': 'PREPAID', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Empty Stomach', 'type': 'VITAL_TAKEN_STATE', 'code': 'EMPTY_STOMACH', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'After Food', 'type': 'VITAL_TAKEN_STATE', 'code': 'AFTER_FOOD', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Before Food', 'type': 'VITAL_TAKEN_STATE', 'code': 'BEFORE_FOOD', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Low', 'type': 'LEVEL', 'code': 'LOW', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'High', 'type': 'LEVEL', 'code': 'HIGH', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Equal to', 'type': 'RELATION', 'code': 'EQUAL_TO', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Less than', 'type': 'RELATION', 'code': 'LESS_THAN', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Greater than', 'type': 'RELATION', 'code': 'GREATER_THAN', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Between', 'type': 'RELATION', 'code': 'BETWEEN', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Accepted', 'type': 'REQUEST_STATUS', 'code': 'ACCEPTED', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Canceled', 'type': 'REQUEST_STATUS', 'code': 'CANCELED', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Enabled', 'type': 'REQUEST_MONITORING_STATUS', 'code': 'ENABLED', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Disabled', 'type': 'REQUEST_MONITORING_STATUS', 'code': 'DISABLED', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Permanently Disabled', 'type': 'REQUEST_MONITORING_STATUS', 'code': 'PERMANENTLY_DISABLED', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Device', 'type': 'VITAL_TYPE', 'code': 'DEVICE', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Device Reading from Apple Watch', 'type': 'VITAL_TYPE', 'code': 'VITAL_READING_FROM_APPLE_WATCH', 'status': True, 'created_at': 'now()', 'created_by': 1},
            {'name': 'Device Reading from Samsung Galaxy Watch', 'type': 'VITAL_TYPE', 'code': 'VITAL_READING_FROM_SAMSUNG_GALAXY_WATCH', 'status': True, 'created_at': 'now()', 'created_by': 1},
        ]

        for enum_item_data in enum_data:
            EnumModel.objects.create(**enum_item_data)
            self.stdout.write(self.style.SUCCESS(f'Enum item {enum_item_data["name"]} created successfully.'))

        self.stdout.write(self.style.SUCCESS('Enum data seeded successfully.'))
