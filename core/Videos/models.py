from asyncio.windows_events import NULL
from unicodedata import category, decimal
from django.db import models

from core.settings import LANGUAGE_CODE
from uuid import uuid4

class Channel(models.Model):
    name =          models.CharField(max_length=255)
    about =         models.TextField(blank=True)
    views =         models.IntegerField(default=0)
    url =           models.URLField(blank=True)
    location =      models.CharField(max_length=255, blank=True)
    category =      models.CharField(max_length=255, blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
    owner =         models.ForeignKey('auth.User',on_delete=models.SET_DEFAULT, default=1)
    icon =          models.ImageField(upload_to='Videos/Channels/icons/',blank=True)
    banner =        models.ImageField(upload_to='Videos/Channel/banners/',blank=True)
    subscribers =   models.ManyToManyField('auth.User', related_name='subscribers', blank=True)
    videos =        models.ManyToManyField('Video', related_name='videos', blank=True)
    subcriptions =  models.ManyToManyField('Channel', related_name='subscriptions', blank=True)
    playlists =     models.ManyToManyField('Playlist', related_name='playlists', blank=True)

class Playlist(models.Model):
    name =         models.CharField(max_length=255)
    about =        models.TextField(blank=True)
    url =          models.URLField(blank=True)
    videos =       models.ManyToManyField('Video', related_name='playlist_videos', blank=True)
    channel =      models.ForeignKey('Channel', on_delete=models.CASCADE, blank=True, null=True)
    created_at =   models.DateTimeField(auto_now_add=True)
    updated_at =   models.DateTimeField(auto_now=True)


class Video(models.Model):
    name =          models.CharField(max_length=255)
    file =          models.FileField(upload_to='Videos/Videos/',blank=False)
    thumbnail=      models.ImageField(upload_to='Videos/Thumbnails/',blank=True)
    description =   models.TextField(blank=True)
    duration =      models.IntegerField(default=0)
    url =           models.URLField(blank=True)
    views =         models.IntegerField(default=0)
    comments =      models.ManyToManyRel('Comment', related_name='comments', blank=True)
    channel =       models.ForeignKey('Channel',on_delete=models.SET_DEFAULT, default=1)
    likes =         models.ManyToManyField('auth.User', related_name='likes', blank=True)
    dislikes =      models.ManyToManyField('auth.User', related_name='dislikes', blank=True)
    

class Comment(models.Model):
    video =         models.ForeignKey('Video',on_delete=models.SET_DEFAULT, default=1)
    comment =       models.TextField(max_length=1024)
    author =        models.ForeignKey('auth.User',on_delete=models.CASCADE)
    likes =         models.ManyToManyField('auth.User', related_name='likes', blank=True)
    dislikes =      models.ManyToManyField('auth.User', related_name='dislikes', blank=True)
    replies =       models.ManyToManyField('Comment', related_name='replies', blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
