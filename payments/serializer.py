from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Payment
        fields= ("user","amount","stripe_payment_intent","status","created_at")
        