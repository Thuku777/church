from django.urls import path
# from .views import AboutDetailView
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('leaders/', views.team, name='leader'),
]

