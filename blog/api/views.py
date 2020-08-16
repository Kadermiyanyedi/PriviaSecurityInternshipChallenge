from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from .models import Blog
from .forms import BlogModelForm, CommentModelForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class SearchView(TemplateView):
    template_name = "api/index.html"

    def get(self, request, *args, **kwargs):
        q = request.GET.get("q")
        self.results = Blog.objects.filter(title__icontains=q)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        return super().get_context_data(blog_list=self.results, **kwargs)


class BlogListView(ListView):
    model = Blog
    template_name = "api/index.html"
    queryset = Blog.objects.all()
    paginate_by = 2


"""class BlogDetailView(DetailView):
    model = Blog
    template_name = "api/detail.html"""


def BlogDetailView(request, pk):
    post = get_object_or_404(Blog, pk=pk)

    form = CommentModelForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect("detail", pk=pk)
    context = {"post": post, "form": form}
    return render(request, "api/detail.html", context)


class BlogAdd(CreateView):
    model = Blog
    form_class = BlogModelForm
    success_url = reverse_lazy("index")
    template_name = "api/add.html"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
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


class LoginUserView(LoginView):
    template_name = "user/login.html"
    form_class = AuthenticationForm

