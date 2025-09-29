from django.urls import path
from .views import CreatePaymentIntent

urlpatterns = [
    path("create-intent/", CreatePaymentIntent.as_view(), name="create-payment-intent")
]
