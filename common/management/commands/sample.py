from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from common.permissions import AuthenticatedUsers



class Command(BaseCommand):
    def handle(self, *args, **options):
        ct = ContentType.objects.get(app_label='auth', model='user')
        perm = Permission.objects.create(codename='adminprivilege', name='Has admin privilege', 
                                        content_type=ct)
        perm.save()
        self.stdout.write(self.style.SUCCESS("Permissions added"))