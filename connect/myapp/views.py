from multiprocessing import context
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory

from django.http import HttpResponse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout



# def index(request):
#     return HttpResponse("Hello world")

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('Home')

    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('Login')

        context = {'form':form}
        return render(request, 'register.html', {'form':form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Home')
            else:
                messages.info(request, 'Username or password is incorrect')
                return render(request, 'login.html')
    
        context = {}
        return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('Login')


@login_required(login_url='Login')
def home(request):
    context = {}
    return render(request, 'home.html')

@login_required(login_url='Login')
def cryptoMK(request):
    context = {}
    return render(request, 'cryptoMK.html')

@login_required(login_url='Login')
def cryptoEN(request):
    context = {}
    return render(request, 'cryptoEN.html')

@login_required(login_url='Login')
def aiMK(request):
    context = {}
    return render(request, 'aiMK.html')

@login_required(login_url='Login')
def aiEN(request):
    context = {}
    return render(request, 'aiEN.html')

@login_required(login_url='Login')
def ipMK(request):
    context = {}
    return render(request, 'ipMK.html')

@login_required(login_url='Login')
def ipEN(request):
    context = {}
    return render(request, 'ipEN.html')

@login_required(login_url='Login')
def oopMK(request):
    context = {}
    return render(request, 'oopMK.html')

@login_required(login_url='Login')
def oopEN(request):
    context = {}
    return render(request, 'oopEN.html')

@login_required(login_url='Login')
def coursesEN(request):
    context = {}
    return render(request, 'coursesEN.html')

@login_required(login_url='Login')
def coursesMK(request):
    context = {}
    return render(request, 'coursesMK.html')
