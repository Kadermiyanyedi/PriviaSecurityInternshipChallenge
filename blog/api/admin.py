from django.contrib import admin
from .models import Blog, Comment


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "author", "date")
    list_filter = ("title", "id", "date")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "comment_author", "date")
    list_filter = ("post", "date")


admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)

admin.site.site_title = "Privia Staj CRUD Blog Api"
