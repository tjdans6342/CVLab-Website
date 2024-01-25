# from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from braces.views import LoginRequiredMixin

from user.models import User
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "post/post_list.html"
    paginate_by = 8


class PostDetailView(DetailView):
    model = Post
    template_name = "post/post_detail.html"
    pk_url_kwarg = "post_id"


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/post_form.html"

    def form_valid(self, form):
        form.instance.author = User.objects.first()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})


# class PostUpdateView(LoginRequiredMixin, UpdateView):
#     model = Post
#     form_class = PostForm
#     template_name = "post/post_form.html"
#     pk_url_kwarg = "post_id"

#     def get_success_url(self):
#         return reverse("post-detail", kwargs={"post_id": self.object.id})
