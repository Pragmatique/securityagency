from django.conf.urls import url, include
from rest_framework import routers
from .views import PaymentConditionsViewSet

router = routers.DefaultRouter()
router.register(r'', PaymentConditionsViewSet)


urlpatterns = [
    url(r'payment-conditions/', include(router.urls)),
]