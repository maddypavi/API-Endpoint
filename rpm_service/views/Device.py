from rest_framework import viewsets
from rpm_service.models import DeviceModel
from rpm_service.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    
    '''API ENDPOINT FOR CONNECTIVITY'''


    queryset = DeviceModel.objects.all()
    serializer_class = DeviceSerializer
    
    