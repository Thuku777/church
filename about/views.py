from django.shortcuts import render
from .models import *

# Create your views here.
def about(request):
    about = About.objects.all()
    return render(request, 'about/about.html', {'about': about})

def team(request):
    leader = Leader.objects.all()
    return render(request, 'about/team.html', {'leader': leader})

