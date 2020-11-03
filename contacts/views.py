from django.shortcuts import render
from .models import *

# Create your views here.
def contact(request):
    contact = ChurchContact.objects.all()
    return render(request, 'contacts/contact.html', { 'contact': contact })