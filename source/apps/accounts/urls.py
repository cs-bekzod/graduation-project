from django.urls import path
from apps.accounts.views import register,profile,UserLogin

urlpatterns = [
    path('auth/login', UserLogin, name='UserLogin'),
    path('auth/register', register, name='register'),
    path('profile/', profile, name='profile'),
]