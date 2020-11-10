from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone
from PIL import Image

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)   

    class Meta:
        verbose_name = 'Photo Category' 
        verbose_name_plural = 'Photo Categories'

    def __str__(self):           
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=120)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='images/Media-team/%Y/%m/%d/', null=True, blank=False)
    # photo_by = models.CharField(max_length=100)
    is_published = models.BooleanField(default=True)
    date_posted = models.DateField(auto_now_add=True)

    @property
    def image_preview(self):
        if self.photo:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.photo.url))
        return "" 

    class Meta:
        verbose_name = 'Photo Gallery'
        verbose_name_plural = 'Photo Gallery'
        ordering = ['date_posted']

    def __str__(self):
        return self.title

