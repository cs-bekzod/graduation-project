from django.contrib import messages
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from apps.accounts.forms import UserRegistrationForm,UserLoginForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        RegisterForm = UserRegistrationForm(request.POST)
        if RegisterForm.is_valid():
            RegisterForm.save()
            
            return redirect('profile')
    else:
        RegisterForm = UserRegistrationForm()
        
    return render(request, 'register.html', {'RegisterForm': RegisterForm})
  

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username','as')
        password = request.POST.get('password','as')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('UserLogin')
    else:
        return render(request, 'login.html')
        

def profile(request):
    
    return render(request, 'student_profile.html')
