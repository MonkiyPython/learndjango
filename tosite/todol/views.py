from django.shortcuts import render  # noqa
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")