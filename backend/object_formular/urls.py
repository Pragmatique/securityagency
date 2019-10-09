from django.conf.urls import url, include
from rest_framework import routers
from .views import ObjectFormularViewSet

router = routers.DefaultRouter()
router.register(r'', ObjectFormularViewSet)


urlpatterns = [
    url(r'object-formular/', include(router.urls)),
]