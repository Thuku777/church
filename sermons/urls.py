from django.urls import path

from . import views

urlpatterns = [
    path('sermons', views.sermon, name='sermon'),
]
