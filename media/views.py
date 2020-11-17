from django.shortcuts import render, get_object_or_404

from .models import Photo, Category

from .models import *
from events.models import *
from sermons.models import *
from about.models import *
from pages.models import *

# Create your views here.
def photo(request):
    slide = Slide.objects.order_by('date_posted').filter(is_published=True)
    event = Event.objects.order_by('date_posted')
    sermon = Sermon.objects.order_by('date_posted')
    about = About.objects.all()
    leader = Leader.objects.all()
    photo = Photo.objects.all()
    category = Category.objects.all()

    context = {
        'slide': slide,
        'event': event,
        'sermon': sermon,
        'about': about,
        'leader': leader,
        'photo': photo,
        'category': category,
    }

    return render (request, 'media/media.html', context)