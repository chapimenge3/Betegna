from django.urls import path 


from .views import Homepage, Login, LogoutView

urlpatterns = [
    path('', Homepage.as_view(), name='index'), 
    path('login/', Login.as_view() , name='login'), 
    path('logout/', LogoutView.as_view() , name='logout'), 
]
