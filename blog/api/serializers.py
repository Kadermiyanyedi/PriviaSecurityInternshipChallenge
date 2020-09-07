from rest_framework import serializers
from .models import Blog, Comment
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Blog
        fields = ("id", "author", "title", "detail", "image", "date", "comments")

    def get_comments(self, obj):
        result = Comment.objects.filter(post_id=obj.id).values_list('comment_author', flat=True)
        return result

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "comment_text", "comment_author", "date")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")
