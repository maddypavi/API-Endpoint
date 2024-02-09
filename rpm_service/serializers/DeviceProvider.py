from rest_framework import serializers
from rpm_service.models import DeviceProviderModel

class DeviceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceProviderModel
        fields = ["name", "enabled"]
