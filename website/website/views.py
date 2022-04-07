from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

def index(request):
    return TemplateView.as_view(template_name='website/templates/index.html', extra_context={'title': 'Home'})(request)

def about(request):
    return render(request, 'website/templates/about.html', context={'title': 'About'})

def contact(request):
    return render(request, 'website/templates/contact.html', context={'title': 'Contact'})



