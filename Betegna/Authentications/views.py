from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate

from .forms import SignUpForm

class Homepage(TemplateView):
    template_name = 'index.html'
    
class Login(LoginView):
    redirect_authenticated_user = True

class Register(TemplateView):
    template_name = 'registration/register.html'
    
    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form})
 
    
        
    