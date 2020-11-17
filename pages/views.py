from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core import serializers
from django.contrib import messages

from .forms import ContactForm
from .models import *
from events.models import *
from sermons.models import *
from about.models import *
from media.models import *

# Create your views here.

def index(request):
    slide = Slide.objects.order_by('date_posted').filter(is_published=True)
    event = Event.objects.order_by('date_posted')[:4]
    sermon = Sermon.objects.order_by('date_posted')[:3]
    about = About.objects.all()
    leader = Leader.objects.all()
    photo = Photo.objects.all()
            
    context = {
        'slide': slide,
        'event': event,
        'sermon': sermon,
        'about': about,
        'leader': leader,
        'photo': photo,
    }
    return render(request, 'pages/index.html', context)


def contact_us(request):
    form = ContactForm()
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']
            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['thukuelvys@gmail.com'])
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            data = {
                'message': 'Data is submitted'
            }
            return JsonResponse(data)
   
    return render(request, 'pages/contact-us.html', {'form': form})

 