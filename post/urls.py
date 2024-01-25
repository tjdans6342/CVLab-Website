# "domain/posts/"

from django.urls import path

from . import views

urlpatterns = [
    # post
    # path("", views.post_list, name="post-list"),
    path("", views.PostListView.as_view(), name="post-list"),
    path("<int:post_id>/", views.PostDetailView.as_view(), name="post-detail"),
    path("new/", views.PostCreateView.as_view(), name="post-create"),
    # path('<int:post_id>/edit/', views.PostUpdateView.as_view(), name='post-update'),
    # path('<int:post_id>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
