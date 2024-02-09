

from typing import Any
from django.core.management.base import BaseCommand
from rpm_service.models import ConnectivityTypeModel



class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        
        items = [
            {
                "name": "BLUETOOTH",
                "description": "Bluetooth connectivity"
            },
            {
                "name": "WIFI",
                "description": "Wifi connectivity"
            }
        ]
        
        for item in items:
            ConnectivityTypeModel.objects.create(**item)
            self.stdout.write(self.style.SUCCESS(f"Successfully created {item['name']}"))
        
        self.stdout.write(self.style.SUCCESS("Successfully seeded connectivity types"))