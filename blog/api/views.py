from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Blog, Comment
from .forms import BlogModelForm, CommentModelForm
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Blog
    template_name = "api/index.html"
    queryset = Blog.objects.all()


class BlogDetailView(DetailView):
    model = Blog
    login_required = True
    template_name = "api/detail.html"


class BlogAdd(CreateView):
    model = Blog
    form_class = BlogModelForm
    success_url = reverse_lazy("index")
    template_name = "api/add.html"

    def form_valid(self, form):
        return super().form_valid(form)


class BlogUpdate(UpdateView):
    model = Blog
    fields = ["title", "detail", "image"]
    template_name = "api/edit.html"
    success_url = reverse_lazy("index")


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "api/delete.html"
    success_url = reverse_lazy("index")


class CommentListView(ListView):
    model = Comment
    template_name = "api/comment_list.html"
    queryset = Comment.objects.all()


class CommentAdd(CreateView):
    model = Comment
    form_class = CommentModelForm
    success_url = reverse_lazy("")
    template_name = "api/comment_add.html"

    def form_valid(self, form):
        return super().form_valid(form)
