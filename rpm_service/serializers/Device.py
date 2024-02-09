from django.db import models

from rest_framework import serializers
from rpm_service.models import DeviceModel

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = "__all__"