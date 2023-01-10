from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('event_list', views.event_list, name='event_list'),
]