from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import PaymentConditions
from .serializers import PaymentConditionsSerializer

# Create your views here.

class PaymentConditionsViewSet(viewsets.ModelViewSet):
    queryset = PaymentConditions.objects.all()
    serializer_class = PaymentConditionsSerializer
    permission_classes = [permissions.IsAuthenticated]