from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
import cprint

def login_view(request):
    if request.method == "GET":
        my_form = Login_form()
        return render(request, 'login.html', {'my_form': my_form})

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile',user.pk)
           
            # profile(1)
        else:
            return redirect('login')

# *_______________________________________________________

def logout_view(request):
    logout(request)
    return redirect ('login')

# *_______________________________________________________


def profile(request,pk):
    return render (request,'profile.html')

    