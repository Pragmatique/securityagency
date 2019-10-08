from rest_framework import serializers
from .models import ProjectStatus, PropertyType, ServiceType, ObjectType, PaymentType, MainContractors, ClientType

class ProjectStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectStatus
        fields = ('id','status')

class PropertyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyType
        fields = ('id','property_type')

class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceType
        fields = ('id','service_type')

class ObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ('id','object_type')

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('id','payment_type')

class MainContractorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainContractors
        fields = ('id','contractor')

class ClientTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientType
        fields = ('id','type')