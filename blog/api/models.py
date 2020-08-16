from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        "api.Blog", on_delete=models.CASCADE, related_name="comments"
    )
    comment_text = models.TextField()
    comment_author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for the {self.post}"

