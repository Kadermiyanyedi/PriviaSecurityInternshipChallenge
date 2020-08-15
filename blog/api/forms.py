from django import forms
from .models import Blog, Comment


class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "detail", "image"]


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_text", "comment_author"]

