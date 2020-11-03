from django.db import models
from django.utils import timezone

# Create your models here.
class Ministry(models.Model):
    name = models.CharField(max_length=100)
    chairperson = models.CharField(max_length=100)
    vice_chairperson = models.CharField(max_length=100)
    treasurer = models.CharField(max_length=100)
    secretary = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    date_posted = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'Ministry'
        verbose_name_plural = 'Ministries'
        ordering = ['date_posted']

    def __str__(self):
        return self.name