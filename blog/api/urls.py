from django.urls import path
from .views import (
    BlogAdd,
    BlogDeleteView,
    BlogDetailView,
    BlogListView,
    BlogUpdate,
    LoginUserView,
    SearchView,
)
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", LoginUserView.as_view(), name="login"),
    path("index/", BlogListView.as_view(), name="index"),
    path("add/", BlogAdd.as_view(), name="add"),
    path("detail/<int:pk>", BlogDetailView, name="detail"),
    path("delete/<int:pk>", BlogDeleteView.as_view(), name="delete"),
    path("update/<int:pk>", BlogUpdate.as_view(), name="update"),
    path("search/", SearchView.as_view(), name="search"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

