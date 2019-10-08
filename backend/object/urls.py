from django.conf.urls import url, include
from rest_framework import routers
from .views import ObjectViewSet

router = routers.DefaultRouter()
router.register(r'', ObjectViewSet)


urlpatterns = [
    url(r'object/', include(router.urls)),
]