from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "author", "title", "detail", "image", "date")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "comment_text", "comment_author", "date")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
