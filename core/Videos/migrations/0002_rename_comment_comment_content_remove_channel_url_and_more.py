# Generated by Django 4.0.3 on 2022-04-09 18:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Videos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='channel',
            name='url',
        ),
        migrations.RemoveField(
            model_name='playlist',
            name='url',
        ),
        migrations.RemoveField(
            model_name='video',
            name='url',
        ),
        migrations.AddField(
            model_name='channel',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='replies',
            field=models.ManyToManyField(blank=True, related_name='comment_replies', to='Videos.comment'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='channel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Videos.channel'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='playlist',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='playlist',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='channel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='Videos.channel'),
        ),
        migrations.AddField(
            model_name='video',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='video_comments', to='Videos.comment'),
        ),
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='video_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
        migrations.AddField(
            model_name='video',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='channel',
            name='banner',
            field=models.ImageField(blank=True, upload_to='Videos/Channel/banners/'),
        ),
        migrations.AlterField(
            model_name='channel',
            name='icon',
            field=models.ImageField(blank=True, upload_to='Videos/Channels/icons/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(upload_to='Videos/Videos/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='Videos/Thumbnails/'),
        ),
    ]
