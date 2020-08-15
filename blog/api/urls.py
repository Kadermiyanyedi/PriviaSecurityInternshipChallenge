from django.urls import path
from .views import BlogAdd, BlogDeleteView, BlogDetailView, BlogListView, BlogUpdate

urlpatterns = [
    path("", BlogListView.as_view(), name="index"),
    path("add/", BlogAdd.as_view(), name="add"),
    path("detail/<int:pk>", BlogDetailView.as_view(), name="detail"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", BlogUpdate.as_view(), name="update"),
]

