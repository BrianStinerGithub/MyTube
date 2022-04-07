from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

def index(request):
    return render(request, 'index.html', context={'title': 'Home'})

def about(request):
    return render(request, 'about.html', context={'title': 'About'})

def contact(request):
    return render(request, 'contact.html', context={'title': 'Contact'})

def hello(request):
    return render(request, 'hello.html', context={'title': 'Hello'})



