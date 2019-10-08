from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectStatusViewSet, PropertyTypeViewSet, ServiceTypeViewSet, ObjectTypeViewSet, \
    PaymentTypeViewSet, MainContractorsViewSet, ClientTypeViewSet

router = routers.DefaultRouter()
router.register(r'project-status', ProjectStatusViewSet)
router.register(r'property-type', PropertyTypeViewSet)
router.register(r'service-type', ServiceTypeViewSet)
router.register(r'object-type', ObjectTypeViewSet)
router.register(r'payment-type', PaymentTypeViewSet)
router.register(r'main-contractors', MainContractorsViewSet)
router.register(r'client-type', ClientTypeViewSet)


urlpatterns = [
    url(r'dictionary/', include(router.urls)),
]