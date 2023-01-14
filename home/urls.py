from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("contact", views.contact, name="contact"),
    path("logout", views.logout, name="logout"),
    path("fix", views.fix, name="fix"),
    path("eventpage/<str:id>", views.eventpage, name="eventpage"),
    path('event_list', views.event_list, name='event_list'),
]