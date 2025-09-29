from rest_framework import serializers
from .models import Blog, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ["id","user","text","created_at"]


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.email")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model=Blog
        fields=["id","title","content","author","created_at","updated_at","comments","blog_image"]


    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.blog_image:
            data["blog_image"] = instance.blog_image.url
        return data

