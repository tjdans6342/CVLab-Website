# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def profile(request, pk):
    return HttpResponse(f"유저 아이디가 {pk}인 profile 페이지")
