import uuid
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from . import models

def home(request):
    homepage_videos = models.Video.objects.all()
    return render(request, 'home.html', {'videos': homepage_videos})

def upload(request):
    return render(request, 'upload.html')

def profile(request):
    return render(request, 'profile.html')


def watch_video(request, video_id):
    video = models.Video.objects.get(uuid=video_id)
    return render(request, 'watch_video.html', {'video': video})

@require_http_methods(["POST"])
def update_video(request, video_id):
    video = models.Video.objects.get(id=video_id)
    video.complete = not video.complete
    video.save()
    return render(request, 'update_video.html', {'video': video})

def delete_video(request, video_id):
    return redirect("index")

def get_playlist(request, playlist_id):
    return render(request, 'get_playlist.html')

def add_playlist(request):
    return render(request, 'add_playlist.html')

def update_playlist(request, playlist_id):
    return render(request, 'update_playlist.html')

def delete_playlist(request, playlist_id):
    return render(request, 'delete_playlist.html')


def get_channel(request, channel_id):
    return render(request, 'get_channel.html')

def add_channel(request):
    return render(request, 'add_channel.html')

def update_channel(request, channel_id):
    return render(request, 'update_channel.html')

def delete_channel(request, channel_id):
    return render(request, 'delete_channel.html')


def get_comment(request, comment_id):
    return render(request, 'get_comment.html')

def add_comment(request):
    return render(request, 'add_comment.html')

def update_comment(request, comment_id):
    return render(request, 'update_comment.html')

def delete_comment(request, comment_id):
    return render(request, 'delete_comment.html')

