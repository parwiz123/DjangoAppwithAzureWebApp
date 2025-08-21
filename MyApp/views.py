from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello World, This is django runing on azure app service</h1>")
