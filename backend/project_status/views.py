from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework import permissions

from .models import ProjectStatus, PropertyType, ServiceType, ObjectType, PaymentType, MainContractors, ClientType
from .serializers import ProjectStatusSerializer, PropertyTypeSerializer, ServiceTypeSerializer, ObjectTypeSerializer, \
    PaymentTypeSerializer, MainContractorsSerializer, ClientTypeSerializer

# Create your views here.
class ProjectStatusViewSet(viewsets.ModelViewSet):
    queryset = ProjectStatus.objects.all()
    serializer_class = ProjectStatusSerializer
    permission_classes = [permissions.IsAuthenticated]

class PropertyTypeViewSet(viewsets.ModelViewSet):
    queryset = PropertyType.objects.all()
    serializer_class = PropertyTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ServiceTypeViewSet(viewsets.ModelViewSet):
    queryset = ServiceType.objects.all()
    serializer_class = ServiceTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class ObjectTypeViewSet(viewsets.ModelViewSet):
    queryset = ObjectType.objects.all()
    serializer_class = ObjectTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class PaymentTypeViewSet(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    permission_classes = [permissions.IsAuthenticated]

class MainContractorsViewSet(viewsets.ModelViewSet):
    queryset = MainContractors.objects.all()
    serializer_class = MainContractorsSerializer
    permission_classes = [permissions.IsAuthenticated]

class ClientTypeViewSet(viewsets.ModelViewSet):
    queryset = ClientType.objects.all()
    serializer_class = ClientTypeSerializer
    permission_classes = [permissions.IsAuthenticated]