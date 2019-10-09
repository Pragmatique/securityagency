from django.conf.urls import url, include
from rest_framework import routers
from .views import MountingViewSet

router = routers.DefaultRouter()
router.register(r'', MountingViewSet)


urlpatterns = [
    url(r'mounting/', include(router.urls)),
]