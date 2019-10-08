from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Object
from .serializers import ObjectSerializer

# Create your views here.
class ObjectViewSet(viewsets.ModelViewSet):
    queryset = Object.objects.all()
    serializer_class = ObjectSerializer
    permission_classes = [permissions.IsAuthenticated]