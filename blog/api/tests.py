from django.test import TestCase
from .models import Blog, Comment
from django.urls import reverse
from django.contrib.auth.models import User


class RenewBookFormTest(TestCase):
    def test_post_create(self):
        author = User.objects.create(username="admin", password="admin")
        post = Blog.objects.create(
            author=author, title="text.py", detail="test.py deneme"
        )

    def test_comment_create(self):
        author = User.objects.create(username="admin", password="admin")
        post = Blog.objects.create(
            author=author, title="text.py", detail="test.py deneme"
        )
        comment = Comment.objects.create(
            post=post, comment_author="test", comment_text="test"
        )
        self.assertEqual(post.comments.count(), 1)

    def test_model_str(self):
        author = User.objects.create(username="admin", password="admin")
        post = Blog.objects.create(
            author=author, title="test.py", detail="test.py deneme"
        )

        self.assertEqual(str(post), "test.py")

    def test_title_max_length(self):
        post = Blog
        max_length = post._meta.get_field("title").max_length
        self.assertEquals(max_length, 50)

    def test_can_login(self):
        data = {
            "username": "admin",
            "password": "admin",
        }
        response = self.client.post(reverse("login"), data=data)
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/swagger/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "api/index.html")
