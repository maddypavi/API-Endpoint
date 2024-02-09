from rest_framework import viewsets
from rpm_service.models import ConnectivityTypeModel
from rpm_service.serializers import ConnectivityTypeSerializer


class ConnectivityTypeViewSet(viewsets.ModelViewSet):
    
    '''API ENDPOINT FOR CONNECTIVITY'''


    queryset = ConnectivityTypeModel.objects.all()
    serializer_class = ConnectivityTypeSerializer
    