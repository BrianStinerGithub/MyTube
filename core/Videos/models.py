from unicodedata import category, decimal
from django.db import models

from core.core.settings import LANGUAGE_CODE
from uuid import uuid4

class Course(models.Model):
    name =          models.CharField(max_length=255)
    description =   models.TextField(blank=True)
    category =      models.CharField(max_length=255, blank=False)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    author =        models.ForeignKey('auth0.User',on_delete=models.CASCADE)
    language =      models.CharField(max_length=2,default=LANGUAGE_CODE)
    image_url =     models.ImageField(upload_to='courses/',blank=True)
    price =         models.DecimalField(max_digits=6,decimal_places=2)
    duration =      models.IntegerField()
    rating =        models.DecimalField(max_digits=3,decimal_places=2)
    course_uuid =   models.UUIDField(primary_key=True,default=uuid4,editable=False)
    course_sections=models.ManyToManyField('Section',blank=True)

class Section(models.Model):
    name =          models.CharField(max_length=255)
    description =   models.TextField(blank=True)
    episodes =      models.ManyToManyField('Episode',blank=True)

class Episode(models.Model):
    name =          models.CharField(max_length=255)
    file =          models.FileField(upload_to='episodes')
    description =   models.TextField(blank=True)
    duration =      models.IntegerField(max_length=10, decimal_places=0)
    url =           models.URLField(blank=True)
    thumbnail=      models.ImageField(upload_to='episode_images',blank=True)

class Comment(models.Model):
    comment =       models.TextField(max_length=1024)
    author =        models.ForeignKey('auth0.User',on_delete=models.CASCADE)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    episode =       models.ForeignKey('Episode',on_delete=models.CASCADE)