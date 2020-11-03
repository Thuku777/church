from django.db import models
from django.utils import timezone
from embed_video.fields import EmbedVideoField

# Create your models here.
class Sermon(models.Model):
    title = models.CharField(max_length=100)
    # sermon = models.VideoURLField(max_length=200, help_text="Add the link of the sermon from youtube or facebook")
    sermon = EmbedVideoField(max_length=200, help_text="Add the link of the sermon from youtube or facebook")
    created_by = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Sermon'
        verbose_name_plural = 'Sermons'
        ordering = ['date_posted']

    def __str__(self):
        return self.title
