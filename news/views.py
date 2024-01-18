# from django.shortcuts import render
from django.http import HttpResponse


def news_list(request):
    return HttpResponse("news_list function")
