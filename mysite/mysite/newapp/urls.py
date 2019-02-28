from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='newapp-home'),
    path('about', views.home, name='newapp-about'),

    path('contact', views.contact, name='newapp-contact')

]
