from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Mounting
from .serializers import MountingSerializer

# Create your views here.

class MountingViewSet(viewsets.ModelViewSet):
    queryset = Mounting.objects.all()
    serializer_class = MountingSerializer
    permission_classes = [permissions.IsAuthenticated]