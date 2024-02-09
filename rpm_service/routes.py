from rest_framework.routers import DefaultRouter

from rpm_service.views.Device import DeviceViewSet
from rpm_service.views.ConnectivityType import ConnectivityTypeViewSet
from rpm_service.views.DeviceProvider import DeviceProviderViewSet
 


router = DefaultRouter()

# router.register(
#     "alert-type", 
#     AlertTypeViewSet, 
#     basename="alert_type"
# )
router.register(
    "connectivity-type", 
    ConnectivityTypeViewSet, 
    basename="connectivity_type"
)
router.register(
    "device",
    DeviceViewSet,
    basename="device"
)

# router.register(
#     "device-assignment", 
#     DeviceAssignmentViewSet, 
#     basename="device_assignment"
# )
# router.register(
#     "device-imei",
#     DeviceImeiViewSet,
#     basename="device_imei"
# )
# # router.register(
#     "device-imei-available",
#     DeviceImeiAvailableViewSet,
#     basename="device_imei_available"
# )
router.register(
    "device-provider",
    DeviceProviderViewSet,
    basename="device_provider"
)
# router.register(
#     "device-vital",
#     DeviceVitalViewSet,
#     basename="device_vital"
# )
# router.register(
#     "vital",
#     VitalViewSet,
#     basename="vital"
# )
# router.register(
#     "disease-device",
#     DiseaseDeviceViewSet,
#     basename="disease_device"
# )
