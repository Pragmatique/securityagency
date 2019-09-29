from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectStatusViewSet

router = routers.DefaultRouter()
router.register(r'project-status', ProjectStatusViewSet)


urlpatterns = [
    url(r'dictionary/', include(router.urls)),
]