from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from .models import Profile


def index(request):
    return render(request, 'index.html')

def signup(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password1=password1)
                user.save()
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        
        return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')