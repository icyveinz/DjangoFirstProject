from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('home', index, name='home'),
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]