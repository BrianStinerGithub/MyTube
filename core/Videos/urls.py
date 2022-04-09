from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("watch/<str:video_id>", views.watch_video, name="watch_video"),
]