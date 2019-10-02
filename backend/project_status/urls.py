from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectStatusViewSet, PropertyTypeViewSet

router = routers.DefaultRouter()
router.register(r'project-status', ProjectStatusViewSet)
router.register(r'property-type', PropertyTypeViewSet)


urlpatterns = [
    url(r'dictionary/', include(router.urls)),
]