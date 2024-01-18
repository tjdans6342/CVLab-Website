from django.urls import path

from . import views

urlpatterns = [
    path("profile/<int:pk>/", views.profile, name="profile"),
    # path('login/', views.login, ....)
]
