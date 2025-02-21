from django.urls import path
from django.views.generic import TemplateView

from blog import views

urlpatterns = [
    path('', views.index),
    path('template_view/',
         TemplateView.as_view(template_name='blog/index.html', extra_context={
             "age" : 50,
             "languages" : ["ss", "vv"]
         })),
]