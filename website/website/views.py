from django.shortcuts import render
from django.views.generic import TemplateView
from . import models

def home(request):
    return render(request, 'home.html', context={'title': 'Home'})

def about(request):
    return render(request, 'about.html', context={'title': 'About'})

def contact(request):
    return render(request, 'contact.html', context={'title': 'Contact'})

def hello(request):
    return render(request, 'hello.html', context={'title': 'Hello'})



