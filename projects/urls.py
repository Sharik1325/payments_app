from rest_framework import routers
from .api import PaymentViewSet

router = routers.DefaultRouter()
router.register('api/payment-tc/process', PaymentViewSet, 'payment')
urlpatterns = router.urls

