from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["email","username","password"]


    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(password=password, **validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


    def validate(self, data):
            email = data.get("email")
            password = data.get("password")

            if email and password:
                user = authenticate(email=email, password=password)
                if user and user.is_active:
                    data["user"] = user
                    return data
                else :
                    raise serializers.ValidationError("invalid username or passwrod")
            else:
                raise serializers.ValidationError("email and password are required")



