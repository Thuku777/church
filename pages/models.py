from django.db import models
from django.utils.html import mark_safe
from django.utils import timezone
from PIL import Image

# Create your models here.
class Slide(models.Model):
    title = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, blank=False, null=True, unique=True)
    # label = models.CharField(max_length=200)
    description = models.TextField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    is_published = models.BooleanField(default=True)
    image = models.ImageField(upload_to='images/Slides/%Y/%m/%d/', null=True, blank=False)

    @property
    def image_preview(self):
        if self.image:
            return mark_safe('<img src="{}" width="100" height="100" />'.format(self.image.url))
        return "" 
   

    def __str__(self):
        return self.title

    # def save(self, **kwargs):
    #     super().save()
 

    #     img = Image.open(self.image.path)

    #     if img.height > 420 or img.width > 390:
    #         output_size = (420, 390)
    #         img.thumbnail(output_size)
            # img.save(self.image.path)
