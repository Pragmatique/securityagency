from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Client
from .serializers import ClientSerializer

# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAuthenticated]
