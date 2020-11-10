from django.shortcuts import render
from .models import *
# Create your views here.
def sermon(request):
    sermon = Sermon.objects.order_by('date_posted')
    context = { 'sermon': sermon }
    return render(request, 'sermons/sermons.html', context)
    