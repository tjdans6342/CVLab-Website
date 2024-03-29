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
from .models import Gallery

from .forms import GalleryForm


class GalleryListView(ListView):
    model = Gallery
    context_object_name = "galleries"
    template_name = "gallery/gallery_list.html"
    paginate_by = 4


class GalleryDetailView(DetailView):
    model = Gallery
    template_name = "gallery/gallery_detail.html"
    pk_url_kwarg = "gallery_id"


class GalleryCreateView(LoginRequiredMixin, CreateView):
    model = Gallery
    form_class = GalleryForm
    template_name = "gallery/gallery_form.html"

    def form_valid(self, form):  # Image 객체들과 gallery 객체 연결하는 작업 해야 함.
        # form.instance.author = User.objects.first()
        print(self.request.user)
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("gallery-detail", kwargs={"gallery_id": self.object.id})
