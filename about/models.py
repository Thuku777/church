from django.db import models
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.html import mark_safe
from PIL import Image

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100)
    message = models.TextField()
    mission = models.TextField(default='our mission')
    beliefs = models.TextField(default='our beliefs')
    benefits = models.TextField(default='the benefits')
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'About'
        ordering = ['-id']

    def __str__(self):
        return self.title


class Leader(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=400)
    date_posted = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_pastor = models.BooleanField(default=False)
    is_leader = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/Leaders/%Y/%m/%d/', null=True, blank=False)

    # Image preview property in admin area
    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 

    
    class Meta:
        verbose_name = 'Leaders'
        verbose_name_plural = 'DC Kenol Team'
        ordering = ['date_posted']

    def __str__(self):
        return self.name

