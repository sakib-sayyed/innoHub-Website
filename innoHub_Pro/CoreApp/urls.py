from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('services',services,name='services'),
    path('about',aboutUs,name='aboutUs'),
    path('team',team,name='team'),
    path('contact',contactUs,name='contactUs')
]
