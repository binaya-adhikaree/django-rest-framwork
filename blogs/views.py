from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from .pagination import CustomPagination

# Create your views here.
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all().order_by("-created_at")
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    parser_classes = (MultiPartParser, FormParser, JSONParser)
    pagination_class = CustomPagination

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)


class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]
    parser_classes = (MultiPartParser, FormParser, JSONParser)




class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def perform_create(self, serializer):
        blog_id = self.kwargs.get("blog_id")
        serializer.save(user =self.request.user, blog_id = blog_id)
