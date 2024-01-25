from django.urls import include, path

from .views import index

urlpatterns = [
    path("", index, name="index"),
    
    # include other apps
    path("posts/", include("post.urls")),
    path("galleries/", include("gallery.urls")),
    path("news/", include("news.urls")),
]
