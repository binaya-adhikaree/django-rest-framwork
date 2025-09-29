from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

 
class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception= True)
        user= serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)
        return Response({
            "user":{
                "email":user.email,
                "username":user.username
            },
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }) 
    

User = get_user_model()

class SocialLoginSuccess(APIView):
    permission_classes = [AllowAny]  

    def get(self,request, *args, **kwargs):
        user = request.user

        if user.is_anonymous:
            return Response({
                "error":"user is not authenticated"
            },
            status=status.HTTP_401_UNAUTHORIZED
            )
        
        refresh = RefreshToken.for_user(user)
        return Response({
            "user":{
                "email":user.email,
                "username":user.username
            },
            "refresh":str(refresh),
            "access":str(refresh.access_token)
        }) 




    

