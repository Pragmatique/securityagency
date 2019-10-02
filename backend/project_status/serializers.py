from rest_framework import serializers
from .models import ProjectStatus, PropertyType

class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = ('id','status')

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('id','property_type')