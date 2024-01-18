# from django.shortcuts import render
from django.http import HttpResponse


def gallery_list(request):
    return HttpResponse("gallery_list function")
