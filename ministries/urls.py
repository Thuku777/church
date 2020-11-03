from django.urls import path

from . import views

urlpatterns = [
    path('ministries', views.ministry, name='ministry'),
]
