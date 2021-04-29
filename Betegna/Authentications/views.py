from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView


class Homepage(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    redirect_authenticated_user = True