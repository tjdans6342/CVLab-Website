from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    # include other apps
    path("posts/", include("post.urls")),
    path("galleries/", include("gallery.urls")),
    path("news/", include("news.urls")),
]
