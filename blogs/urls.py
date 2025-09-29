from django.urls import path
from .views import BlogListCreateView, BlogDetailView, CommentCreateView
from .models import Blog
from django.contrib import admin


urlpatterns = [
    path("blogs/", BlogListCreateView.as_view(), name="blog-list-create"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog-detail"),

    path("blogs/<int:blog_id>/comments/",CommentCreateView.as_view(), name="comment-create" )
]
