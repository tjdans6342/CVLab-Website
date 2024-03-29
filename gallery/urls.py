from django.urls import path

from . import views

urlpatterns = [
    path("", views.GalleryListView.as_view(), name="gallery-list"),
    path("<int:gallery_id>/", views.GalleryDetailView.as_view(), name="gallery-detail"),
    path("new/", views.GalleryCreateView.as_view(), name="gallery-create"),
]
