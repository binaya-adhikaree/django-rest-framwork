# payments/views.py
import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Payment
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


stripe.api_key = settings.STRIPE_SECRET_KEY


@method_decorator(csrf_exempt, name='dispatch')
class CreatePaymentIntent(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            product_id = request.data.get("product_id")
            if not product_id:
                return Response({"error":"product id is required"}, status=status.HTTP_400_BAD_REQUEST)
            
            try:
                product = Product.objects.get(id=product_id)
            except Product.DoesNotExist:
                return Response({"error":"Product not found"}, status=status.HTTP_404_NOT_FOUND)



            intent = stripe.PaymentIntent.create(
                amount=int(product.price * 100),
                currency="usd",
                payment_method_types=["card"],
                automatic_payment_methods=None,
                metadata= {"user_id":request.user.id, "product_id":product.id}
            )    

            payment =  Payment.objects.create(
                user=request.user,
                product = product,
                amount = product.price,
                stripe_payment_intent = intent["id"],
                status= "pending"
            )

            return Response({
                "clientsecret": intent["client_secret"],
                "paymentId":payment.id,
                "product":product.name,
                "price":product.price
            }, status=status.HTTP_201_CREATED)



        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)    
