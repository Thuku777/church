from django.db import models
from django.utils import timezone
from ministries.models import Ministry

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the upcoming event")
    title = models.CharField(max_length=100, help_text="eg. Conference, Meeting etc")
    ministry = models.ForeignKey(Ministry, on_delete=models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(max_length=1000)
    fee = models.CharField(max_length=100, help_text="If free write free otherwise input the amount")
    location = models.CharField(max_length=100, help_text="Location of the event")
    date = models.CharField(max_length=250, help_text="eg. 20th September 2020 to 30th September 2020")
    time = models.CharField(max_length=250, help_text="eg. 1030hrs to 1400hrs")
    date_posted = models.DateTimeField(default=timezone.now)
 
    class Meta:
        verbose_name = 'Upcoming Event'
        verbose_name_plural = 'Upcoming Events'

    def __str__(self):
        return self.name



