from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectStatusViewSet, PropertyTypeViewSet, ServiceTypeViewSet, ObjectTypeViewSet

router = routers.DefaultRouter()
router.register(r'project-status', ProjectStatusViewSet)
router.register(r'property-type', PropertyTypeViewSet)
router.register(r'service-type', ServiceTypeViewSet)
router.register(r'object-type', ObjectTypeViewSet)


urlpatterns = [
    url(r'dictionary/', include(router.urls)),
]