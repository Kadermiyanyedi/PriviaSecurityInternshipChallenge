from django.db import models


class Blog(models.Model):
    id = models.IntegerField(primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    detail = models.TextField()
    image = models.ImageField(blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField()
    comment_author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment for the {self.post}"

