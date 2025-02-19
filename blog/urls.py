from django.urls import path
from .views import index, about, contact

urlpatterns = [
    path('home', index, name='home'),
    path('about', about, name='about', kwargs={'name':'Egor', 'age':25}),
    path('contact/<str:street>/<str:building>/', contact, name='contact'),
    path('contact/', contact, name='contact'),
]