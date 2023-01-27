from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = ('id', 'name', 'surname', 'card_number', 'card_cvv', 'total_value', 'extra_description')
        read_only = ('comission_value',)

