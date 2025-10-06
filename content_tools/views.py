from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import GeneratedContent
from .serializers import GeneratedContentSerializer
from .services.openai_client import generate_content
from rest_framework.permissions import IsAuthenticated, AllowAny

from rest_framework.permissions import AllowAny

class GenerateContentView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        prompt = request.data.get("prompt", "")
        if not prompt:
            return Response({"error": "Prompt is required"}, status=400)

        result = generate_content(prompt)

        user = request.user if request.user.is_authenticated else None

        content = GeneratedContent.objects.create(
            user=user,
            prompt=prompt,
            result=result
        )

        serializer = GeneratedContentSerializer(content)
        return Response(serializer.data, status=201)