from django.conf.urls import url, include
from rest_framework import routers
from .views import ProjectViewSet

router = routers.DefaultRouter()
router.register(r'', ProjectViewSet)

urlpatterns = [
    url(r'project/', include(router.urls)),
]