from django.conf.urls import url, include
from rest_framework import routers
from .views import UserViewSet, UserProfileViewSet, UserPartialUpdateView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'userprofiles', UserProfileViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^users/update-partial/(?P<pk>\d+)/', UserPartialUpdateView.as_view(), name='user_partial_update'),
]