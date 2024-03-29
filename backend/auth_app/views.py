from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from .models import User, UserProfile
from .serializers import UserSerializer, UserProfileSerializer, SimpleUserSerializer
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    # def get_permissions(self):
    #     permission_classes = []
    #     if self.action == 'create':
    #         permission_classes = [AllowAny]
    #     elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
    #         permission_classes = [IsLoggedInUserOrAdmin]
    #     elif self.action == 'list' or self.action == 'destroy':
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserPartialUpdateView(GenericAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = SimpleUserSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)