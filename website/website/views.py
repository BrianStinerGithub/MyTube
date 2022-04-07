from django.shortcuts import render, redirect
from . import models

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def hello(request):
    return render(request, 'hello.html')


