from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, "Shop/index.html")


def about(request):
    return HttpResponse("we are in about section")


def contact(request):
    return HttpResponse("we are in contact section")


def tracker(request):
    return HttpResponse("we are in tracker section")


def search(request):
    return HttpResponse("we are in search section")


def prodview(request):
    return HttpResponse("we are in productview section")


def checkout(request):
    return HttpResponse("we are in checkout section")
