from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Video)
admin.register(models.Channel)
admin.register(models.Playlist)
admin.register(models.Comment)