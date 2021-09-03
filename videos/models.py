from django.db import models

# Create your models here.

# Models for videos
class Video(models.Model):
  title = models.CharField(max_length=220)
  description = models.TextField(blank=True, null=True)
  slug = models.SlugField(blank=True, null=True) ###
  video_id = models.CharField(max_length=220)
  active = models.BooleanField(default=True)

# Video Proxy
class VideoAllProxy(Video): ###
  class Meta:
    proxy = True
    verbose_name = 'All Video'
    verbose_name_plural = 'All Videos'

# Published videos proxy
class VideoPublishedProxy(Video):
  class Meta:
    proxy = True
    verbose_name = 'Published Video'