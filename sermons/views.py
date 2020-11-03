from django.shortcuts import render
from .models import *
# Create your views here.
def sermon(request):
    sermon = Sermon.objects.all()
    context = { 'sermon': sermon }
    return render(request, 'sermons/sermons.html', context)