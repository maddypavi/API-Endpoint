from django.db import models

from rest_framework import serializers
from rpm_service.models import ConnectivityTypeModel

class ConnectivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectivityTypeModel
        fields = ["name", "description"]
