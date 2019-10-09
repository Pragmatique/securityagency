from rest_framework import serializers
from .models import ObjectFormular

class ObjectFormularSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectFormular
        exclude = ()