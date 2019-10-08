from rest_framework import serializers
from .models import PaymentConditions

class PaymentConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentConditions
        exclude = ()