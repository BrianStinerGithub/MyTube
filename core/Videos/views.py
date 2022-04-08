from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from . import models

def home(request):
    return render(request, 'home.html')

def upload(request):
    return render(request, 'upload.html')

def profile(request):
    return render(request, 'profile.html')

@require_http_methods(["POST"])
def add(request):
    # if request.method == "POST":
    title = request.POST["title"]
    todo = Todo(title=title)
    todo.save()
    return redirect("index")


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.complete = not todo.complete
    todo.save()
    return redirect("index")


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()
    return redirect("index")

def get_video(request, video_id):
    return render(request, 'get_video.html')

def add_video(request):
    return render(request, 'add_video.html')

def update_video(request, video_id):
    return render(request, 'update_video.html')

def delete_video(request, video_id):
    return render(request, 'delete_video.html')


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

