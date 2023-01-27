from .models import Payment
from rest_framework import viewsets, permissions
from .serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    print("PaymentViewSet------>")
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

