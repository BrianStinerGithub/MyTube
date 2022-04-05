from django.shortcuts import render
from django.http import HttpResponse
from os import path


def hello(request):
    return render(request, path.abspath('test/hello.html'))

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")