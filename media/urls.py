from django.urls import path
from . import views

urlpatterns = [
    path('media/', views.Photo, name='media'),
]