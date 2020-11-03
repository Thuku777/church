from django.shortcuts import render
from .models import *

# Create your views here.
def ministry(request):
    ministry = Ministry.objects.all()
    context = { 'ministry': ministry }
    return render(request, 'ministries/ministries.html', context)