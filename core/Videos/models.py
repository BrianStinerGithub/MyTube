from unicodedata import category, decimal
from django.db import models
from core.settings import LANGUAGE_CODE
from uuid import uuid4

# Editable = True so we can view to UUID in the admin. 
# TODO: Make this editable=False before deployment.

class Channel(models.Model):
    uuid =          models.UUIDField(default=uuid4, editable=True, unique=True)
    name =          models.CharField(max_length=255)
    about =         models.TextField(blank=True)
    views =         models.IntegerField(default=0)
    location =      models.CharField(max_length=255, blank=True)
    category =      models.CharField(max_length=255, blank=True)
    owner =         models.ForeignKey('auth.User',on_delete=models.SET_DEFAULT, default=1)
    icon =          models.ImageField(upload_to='Videos/Channels/icons/',blank=True)
    banner =        models.ImageField(upload_to='Videos/Channels/banners/',blank=True)
    subscribers =   models.ManyToManyField('auth.User', related_name='subscribers', blank=True)
    videos =        models.ManyToManyField('Video', related_name='videos', blank=True)
    subcriptions =  models.ManyToManyField('Channel', related_name='subscriptions', blank=True)
    playlists =     models.ManyToManyField('Playlist', related_name='playlists', blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)

class Playlist(models.Model):
    uuid =          models.UUIDField(default=uuid4, editable=True, unique=True)
    name =          models.CharField(max_length=255)
    about =         models.TextField(blank=True)
    videos =        models.ManyToManyField('Video', related_name='playlist_videos', blank=True)
    channel =       models.ForeignKey('Channel', on_delete=models.CASCADE, blank=True, null=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)


class Video(models.Model):
    uuid =          models.UUIDField(default=uuid4, editable=True, unique=True)
    name =          models.CharField(max_length=255)
    file =          models.FileField(upload_to='Videos/watch/Videos/',blank=False)
    thumbnail=      models.ImageField(upload_to='Videos/watch/Videos/Thumbnails/',blank=True)
    description =   models.TextField(blank=True)
    duration =      models.IntegerField(default=0)
    comments =      models.ManyToManyField('Comment', related_name='video_comments', blank=True)
    channel =       models.ForeignKey('Channel',on_delete=models.SET_DEFAULT, default=1)
    likes =         models.ManyToManyField('auth.User', related_name='video_likes', blank=True)
    dislikes =      models.ManyToManyField('auth.User', related_name='video_dislikes', blank=True)
    views =         models.IntegerField(default=0)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)

class Comment(models.Model):
    video =         models.ForeignKey('Video',on_delete=models.SET_DEFAULT, default=1)
    content =       models.TextField(max_length=1024)
    author =        models.ForeignKey('auth.User',on_delete=models.CASCADE)
    likes =         models.ManyToManyField('auth.User', related_name='comment_likes', blank=True)
    dislikes =      models.ManyToManyField('auth.User', related_name='comment_dislikes', blank=True)
    replies =       models.ManyToManyField('Comment', related_name='comment_replies', blank=True)
    created_at =    models.DateTimeField(auto_now_add=True)
    updated_at =    models.DateTimeField(auto_now=True)
