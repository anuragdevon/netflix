from datetime import time
from enum import Flag
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from videos.models import Video

from netflix.db.models import PublishStateOptions
from netflix.db.recievers import publish_state_pre_save, slugify_pre_save


# Creating Custom QuerySet
class PlaylistQuerySet(models.QuerySet):        ###
    def published(self):
        now = timezone.now()
        return self.filter(
            state=PublishStateOptions.PUBLISH,
            publish_timestamp__lte = now,
        )

# Creating Custom Manger
class PlaylistManager(models.Manager):          ###
    def get_queryset(self):
        return PlaylistQuerySet(self.model, using=self._db)
        
    def published(self):
        return self.get_queryset().published()

# Creating Playlist Model
class Playlist(models.Model):
    title = models.CharField(max_length=220)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)      ###
    video = models.ForeignKey(Video, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=2, choices=PublishStateOptions.choices, default=PublishStateOptions.DRAFT)      ###
    publish_timestamp = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True, null=True)

    # Invoking Custom Manager
    objects = PlaylistManager()

    @property
    def is_published(self):
        return self.active

# Invoking django signals           ###
pre_save.connect(publish_state_pre_save, sender=Playlist)
pre_save.connect(slugify_pre_save, sender=Playlist)