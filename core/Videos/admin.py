from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Video)
admin.site.register(models.Channel)
admin.site.register(models.Playlist)
admin.site.register(models.Comment)