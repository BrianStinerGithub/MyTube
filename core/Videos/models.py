from asyncio.windows_events import NULL
from unicodedata import category, decimal
from django.db import models

from core.settings import LANGUAGE_CODE
from uuid import uuid4

class Channel(models.Model):
    name =          models.CharField(max_length=255)
    about =         models.TextField(blank=True)
    url =           models.URLField(blank=True)
    location =      models.CharField(max_length=255, blank=True)
    category =      models.CharField(max_length=255, blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    owner =         models.ForeignKey('auth.User',on_delete=models.SET_DEFAULT, default=1)
    icon =          models.ImageField(upload_to='icons/',blank=True)
    banner =        models.ImageField(upload_to='banners/',blank=True)
    subscribers =   models.ManyToManyField('auth.User', related_name='subscribers', blank=True)
    videos =        models.ManyToManyField('Video', related_name='videos', blank=True)
    views =         models.IntegerField(default=0)
    subcriptions =  models.ManyToManyField('Channel', related_name='subscriptions', blank=True)
    playlists =     models.ManyToManyField('Playlist', related_name='playlists', blank=True)

class Playlist(models.Model):
    name =         models.CharField(max_length=255)
    about =        models.TextField(blank=True)
    url =          models.URLField(blank=True)
    videos =       models.ManyToManyField('Video', related_name='playlist_videos', blank=True)

class Video(models.Model):
    name =          models.CharField(max_length=255)
    file =          models.FileField(upload_to='videos/',blank=False)
    description =   models.TextField(blank=True)
    duration =      models.IntegerField(default=0)
    url =           models.URLField(blank=True)
    thumbnail=      models.ImageField(upload_to='episode_images',blank=True)

class Comment(models.Model):
    comment =       models.TextField(max_length=1024)
    author =        models.ForeignKey('auth.User',on_delete=models.CASCADE)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    video =         models.ForeignKey('Video',on_delete=models.SET_DEFAULT, default=1)