from django.shortcuts import render
from .models import *

# Create your views here.
def event(request):
    event = Event.objects.all()
    context = {'event': event }
    return render(request, 'events/events.html', context)