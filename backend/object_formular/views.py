from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import ObjectFormular
from .serializers import ObjectFormularSerializer

# Create your views here.

class ObjectFormularViewSet(viewsets.ModelViewSet):
    queryset = ObjectFormular.objects.all()
    serializer_class = ObjectFormularSerializer
    permission_classes = [permissions.IsAuthenticated]
