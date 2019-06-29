from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home-home'),
    path('contacts/', views.contacts, name = 'home-contacts')
]
