from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
   slide = Slide.objects.order_by('date_posted').filter(is_published=True)
   context = {
      'slide': slide,
   }
   return render(request, 'pages/index.html', context)



