from django.conf.urls import url, include
from rest_framework import routers
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'', ContactViewSet)


urlpatterns = [
    url(r'contact/', include(router.urls)),
]