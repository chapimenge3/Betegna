from django.urls import path 
from django.contrib.auth import views as auth_views

from .views import Homepage

urlpatterns = [
    path('', Homepage.as_view(), name='index'), 
    path('login/', auth_views.LoginView.as_view() , name='login'), 
]
