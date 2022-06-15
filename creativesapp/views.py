from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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
        
        return render(request, 'feed.html')
    
        
def login(request):
    if request.method == 'POST':
        # form = AuthenticationForm(data=request.POST)
        # if form.is_valid():
        #     user = form.get_user()
        #     login(user)
        #     return redirect('feed')
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('feed')
        else:
            messages.info(request, 'username non existent')
            return redirect('signup')
    else:
        #form = AuthenticationForm()    
        return render(request, 'login.html')

@login_required(login_url='login')
def feed(request):
    return render(request, 'feed.html')

def logout(request):
    auth.logout(request)
    return redirect('logout')