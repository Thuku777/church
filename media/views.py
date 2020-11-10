from django.shortcuts import render, get_object_or_404
from .models import Photo, Category

# Create your views here.
def photo(request):
    photo = Photo.objects.all()
    category = Category.objects.all()
    return render (request, 'media/media.html', {'photo': photo, 'category': category})