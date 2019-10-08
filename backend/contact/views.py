from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .models import Contact
from .serializers import ContactSerializer

# Create your views here.

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]