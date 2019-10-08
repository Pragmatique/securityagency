from django.conf.urls import url, include
from rest_framework import routers
from .views import ClientViewSet

router = routers.DefaultRouter()
router.register(r'', ClientViewSet)


urlpatterns = [
    url(r'client/', include(router.urls)),
]