from django.shortcuts import render
from django.urls import path, include
from django.http import HttpResponse

def index(request):
    return HttpResponse("new entry!")

urlpatterns = [
    path("", index)
]