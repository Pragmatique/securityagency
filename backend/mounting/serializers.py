from rest_framework import serializers
from .models import Mounting

class MountingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mounting
        exclude = ()